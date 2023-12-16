
from datetime import datetime,timedelta
import re
from pathlib import Path
import shutil
import sys

class Field():
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value

class Birthday(Field):

    @Field.value.setter
    def value(self, value):
        if value != None:
            if datetime.today().date() >= datetime.strptime(value, "%d.%m.%Y").date():
                self._value = datetime.strptime(value, "%d.%m.%Y").date()
            else:
                print(f"Incorect birthday date, use format dd.mm.yy")

class Record():
    def __init__(self, name, phones = [],mails = [], birthday = None, address = None) -> None:
        self.name = name
        self.phones = phones
        self.mails = mails
        self.address = address
        self.birthday = Birthday(birthday)

    def __str__(self) -> str:
        return f"Name: {self.name}, Phones: {[phone for phone in self.phones]}, Mails: {[mail for mail in self.mails]}, Birthday: {self.birthday.value}, Address: {self.address}"
    




class PersonalAssistant:
    def __init__(self):
        self.contacts = []
        self.notes = []

    # task 1
    def add_contact(self):
        
        inputs = input('Enter name: ')
        record = Record(inputs)
        inputs = input('Enter phone number: ')
        record.phones.append(inputs)
        inputs = input('Enter maill: ')
        record.mails.append(inputs)
        inputs = input('Enter birthday: ')
        record.birthday = Birthday(inputs)
        inputs = input('Enter address: ')
        record.address = inputs
        self.contacts.append(record)
        


        today = datetime.today()
        next_birthday = today.date() + timedelta(days=20)
        ignor_year = record.birthday.value.replace(year=today.year) #to ignore year
        print(f'vompare nextday: {ignor_year <= next_birthday}')
        print(self.contacts[0].birthday.value)

    # task 2
    def get_birthdays(self):
        days = int(input('Enter amount of days: '))
        today = datetime.today()
        print(f'Today: {today}')
        next_birthday = today.date() + timedelta(days=days)
        for user in self.contacts:
            
            ignor_year = user.birthday.value.replace(year=today.year) #to ignore year
            print(f'ignor_year: {ignor_year}')
            print(f'compare: {today.date() <= ignor_year <= next_birthday}')
            print(f'vompare today: {today.date() <= ignor_year}')
            print(f'vompare nextday: {ignor_year <= next_birthday}')
            print(f'compare actual dates: {datetime(2023,12,26) <= datetime(2024,1,5)}')
            print(f'Today: {today}')
            print(f'next_birthday: {next_birthday}')
            if today.date() <= ignor_year <= next_birthday:
                print('ffffff')
                print(f'\n{user.name}, {user.phones}')

        


    def task_3(self):
        3+3

    def task_4(self):
        4+4

    def task_5(self):
        5+5

    def task_6(self):
        6+6

    def task_7(self):
        7+7

    def task_8(self):
        8+8

    def task_9(self):
        9+9

    def task_10(self):
        10+10

        #  task_11(self):
class CleanFolder():
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    trans = dict()

    for cyrillic, latin in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        trans[ord(cyrillic)] = latin
        trans[ord(cyrillic.upper())] = latin.upper()
        
    def normalize(name: str) -> str:
        translate_name = re.sub(r'\W', '_', name.translate(CleanFolder.trans))
        translate_name = ".".join(translate_name.rsplit("_",1))
        return translate_name

    #--------------------------------------------------
    JPEG_IMAGES = []
    PNG_IMAGES=[]
    JPG_IMAGES = []
    SVG_IMAGES = []
    AVI_VIDEO = []
    MP4_VIDEO = []
    MOV_VIDEO = []
    MKV_VIDEO = []
    DOC_DOCUMENTS = []
    DOCX_DOCUMENTS = []
    TXT_DOCUMENTS = []
    PDF_DOCUMENTS = []
    XLSX_DOCUMENTS = []
    PPTX_DOCUMENTS = []
    MP3_AUDIO = []
    OGG_AUDIO = []
    WAV_AUDIO = []
    AMR_AUDIO = []
    ARCHIVES = []
    MY_OTHERS = []

    REGISTER_EXTENSION = {
        'JPEG': JPEG_IMAGES,
        'PNG': PNG_IMAGES,
        'JPG': JPG_IMAGES,
        'SVG': SVG_IMAGES,
        'AVI': AVI_VIDEO,
        'MP4': MP4_VIDEO,
        'MOV': MOV_VIDEO,
        'MKV': MKV_VIDEO,
        'DOC': DOC_DOCUMENTS,
        'DOCX': DOCX_DOCUMENTS,
        'TXT': TXT_DOCUMENTS,
        'PDF': PDF_DOCUMENTS,
        'XLSX': XLSX_DOCUMENTS,
        'PPTX': PPTX_DOCUMENTS,
        'MP3': MP3_AUDIO,
        'OGG': OGG_AUDIO,
        'WAV': WAV_AUDIO,
        'AMR': AMR_AUDIO,
        'ZIP': ARCHIVES,
        'GZ': ARCHIVES,
        'TAR': ARCHIVES,
    }

    FOLDERS = []
    EXTENSIONS = set()
    UNKNOWN = set()

    def get_extension(name: str) -> str:
        return Path(name).suffix[1:].upper()

    def scan(folder: Path):
        for item in folder.iterdir():
            # Робота з папкою
            if item.is_dir():  # перевіріямо чи обєкт папка
                if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER'):
                    CleanFolder.FOLDERS.append(item)
                    CleanFolder.scan(item)
                continue
            
            # Робота з файлами                    
            extension = CleanFolder.get_extension(item.name) # беремо розширення файлу
            full_name = folder / item.name # беремо повний шлях до файлу
            if not extension:
                CleanFolder.MY_OTHERS.append(full_name)
            else:
                try:
                    ext_reg = CleanFolder.REGISTER_EXTENSION[extension]
                    ext_reg.append(full_name)
                    CleanFolder.EXTENSIONS.add(extension)
                except KeyError:
                    CleanFolder.UNKNOWN.add(extension)
                    CleanFolder.MY_OTHERS.append(full_name)


    def handle_media(file_name: Path, target_folder: Path):
        target_folder.mkdir(exist_ok=True, parents=True)
        file_name.replace(target_folder / CleanFolder.normalize(file_name.name))
        
    def handle_documents(file_name: Path, target_folder: Path):
        target_folder.mkdir(exist_ok=True, parents=True)
        file_name.replace(target_folder / CleanFolder.normalize(file_name.name))
        
    def handle_archive(file_name: Path, target_folder: Path):
        target_folder.mkdir(exist_ok=True, parents=True)
        folder_for_file = target_folder / CleanFolder.normalize(file_name.name.replace(file_name.suffix, ''))
        folder_for_file.mkdir(exist_ok=True, parents=True)
        try:
            shutil.unpack_archive(str(file_name.absolute()), str(folder_for_file.absolute()))
        except shutil.ReadError:
            folder_for_file.rmdir()
            return
        file_name.unlink()

    def main(folder: Path):
        CleanFolder.scan(folder)
        for file in CleanFolder.JPEG_IMAGES:
            CleanFolder.handle_media(file, folder / 'images' / 'JPEG')
        for file in CleanFolder.JPG_IMAGES:
            CleanFolder.handle_media(file, folder / 'images' / 'JPG')  
        for file in CleanFolder.PNG_IMAGES:
            CleanFolder.handle_media(file, folder / 'images' / 'PNG')
        for file in CleanFolder.SVG_IMAGES:
            CleanFolder.handle_media(file, folder / 'images' / 'SVG') 
        for file in CleanFolder.AVI_VIDEO:
            CleanFolder.handle_media(file, folder / 'video' / 'AVI')
        for file in CleanFolder.MP4_VIDEO:
            CleanFolder.handle_media(file, folder / 'video' / 'MP4')
        for file in CleanFolder.MOV_VIDEO:
            CleanFolder.handle_media(file, folder / 'video' / 'MOV')
        for file in CleanFolder.MKV_VIDEO:
            CleanFolder.handle_media(file, folder / 'video' / 'MKV')
        for file in CleanFolder.DOC_DOCUMENTS:
            CleanFolder.handle_documents(file, folder / 'documents' / 'DOC')
        for file in CleanFolder.DOCX_DOCUMENTS:
            CleanFolder.handle_documents(file, folder / 'documents' / 'DOCX')
        for file in CleanFolder.TXT_DOCUMENTS:
            CleanFolder.handle_documents(file, folder / 'documents' / 'TXT')
        for file in CleanFolder.PDF_DOCUMENTS:
            CleanFolder.handle_documents(file, folder / 'documents' / 'PDF') 
        for file in CleanFolder.XLSX_DOCUMENTS:
            CleanFolder.handle_documents(file, folder / 'documents' / 'XLSX')
        for file in CleanFolder.PPTX_DOCUMENTS:
            CleanFolder.handle_documents(file, folder / 'documents' / 'PPTX')
        for file in CleanFolder.MP3_AUDIO:
            CleanFolder.handle_media(file, folder / 'audio' / 'MP3')
        for file in CleanFolder.OGG_AUDIO:
            CleanFolder.handle_media(file, folder / 'audio' / 'OGG')
        for file in CleanFolder.WAV_AUDIO:
            CleanFolder.handle_media(file, folder / 'audio' / 'WAV')
        for file in CleanFolder.AMR_AUDIO:
            CleanFolder.handle_media(file, folder / 'audio' / 'AMR') 
        for file in CleanFolder.MY_OTHERS:
            CleanFolder.handle_media(file, folder / 'MY_OTHER')   
                
        for file in CleanFolder.ARCHIVES:
            CleanFolder.handle_archive(file, folder / 'ARCHIVES') 
        
        for folder in CleanFolder.FOLDERS[::-1]:
            # видаляємо пусті папки після сортування
            try:
                folder.rmdir()
            except OSError:
                print(f'Error during remove: {folder}')
    





def main():
    assistant = PersonalAssistant()
    while True:
        print("\nВведіть команду (для допомоги введіть 'help'):")
        command = input("> ").lower()

        if command == 'help':
            print("Доступні команди: exit")
        elif command == 'add_contact':
            assistant.add_contact()
        elif command == "birthday_day":
            assistant.get_birthdays()
        elif command.lower() == 'clean':
            path = input("Write a path: ")
            
            if Path(path).exists():
                folder_process = Path(path).resolve()
                CleanFolder.main(folder_process)
                print("Done")
            else: 
                print("You wrote a wrong directory")
        elif command == 'exit':
            print("До побачення!")
            break

        else:
            print("Невідома команда. Введіть 'help' для списку доступних команд.")

if __name__ == "__main__":
    main()