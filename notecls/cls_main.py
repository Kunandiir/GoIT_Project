from collections import UserList
from datetime import datetime
import sqlite3


class Note:
    def __init__(self, name, desc, tag) -> None:
        self.name = name
        self.desc = desc
        self.tag = tag
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self) -> str:
        return f'Name: {self.name}\nDesc: {self.desc}\nTag: {self.tag}\nDate: {self.date}'
    

class NoteBook(UserList):
    def __init__(self):
        self.db = sqlite3.connect('notecls/notes.db')
        self.cursor = self.db.cursor()
        super().__init__()
      
      
    def add_note(self, record):
        dict_record = {'name': record.name, 'desc': record.desc, 'tag': record.tag, 'date': record.date}
        self.data.append(dict_record)
        return f'Note successfully added!'
        

    def find_note(self):
        key = input('Введіть параметр(name, desc, tag)>>> ')
        while True:
            if key in ('name', 'desc', 'tag'):
                value = input('Введіть значення>>> ')
                for note in self.data:
                    if value in note[key]:
                        return note
                return f'Нотатки з параметра "{key}" та значенням "{value}" не знайдено.'
            key = input('Ви ввели не правильний параметр\nСпробуйте знову(name, desc, tag)>>> ')


    def change_note(self):
        while True:
            note = self.find_note()
            yn = input(f'{", ".join(note.values())}\nцю нотатку ви бажди знайти?(y/n)>>> ')
            if yn == 'y':
                key = input('Введіть параметр який бажаєте змінити(name, desc, tag)>>> ')
                while True:
                    if key in ('name', 'desc', 'tag'):
                        value = input('Введіть значення>>> ')
                        note[key] = value
                        return note
                    key = input('Ви ввели не правильний параметр\nСпробуйте знову(name, desc, tag)>>> ')   


    def delete_note(self):
        key = input('Введіть параметр(name, desc, tag)>>> ')
        while True:
            if key in ('name', 'desc', 'tag'):
                value = input('Введіть значення>>> ')
                for note in self.data:
                    if value in note[key]: 
                        self.data.remove(note)
                        return f'Нотатку параметра "{key}" та значенням "{value}" успішно видалено!'
                return f'Нотатку з параметром "{key}" та значенням "{value}" не знайдено.'
            key = input('Ви ввели не правильний параметр\nСпробуйте знову(name, desc, tag)>>> ')
    
    
    def load_note(self):
        self.cursor.execute(f"DELETE FROM cls_notes")
        self.db.commit()
        for note in self.data:
            self.cursor.execute("INSERT INTO cls_notes (name, desc, tag, date) VALUES (?, ?, ?, ?)",
                (note['name'], note['desc'], note['tag'], note['date']))
        self.db.commit()
        print('Load')

    def dump_note(self):
        self.cursor.execute("SELECT * FROM cls_notes")
        for note in self.cursor.fetchall():
            dict_note = {'name': note[0], 'desc': note[1], 'tag': note[2], 'date': note[3]}
            self.data.append(dict_note)    
        print('Dump')

    def bye(self):
        print('Good bye!')
        return exit()



def main():
    nbook = NoteBook()
    nbook.dump_note()
    while True:
        try:
            enter = input('Enter command>>> ').lower().strip()
            if enter == 'add-note':
                print(nbook.add_note(Note(input('Enter name>>> '), input('Enter desc>>> '), input('Enter tag>>> '))))
            elif enter == 'find-note':
                print(nbook.find_note())
            elif enter == 'change-note':
                print(nbook.change_note())
            elif enter == 'delete-note':
                print(nbook.delete_note())
            elif enter in ['close', 'exit', 'good bye']:
                print(nbook.bye())
            else:
                print('Wrong command(')
        finally:
            nbook.load_note()
        
if __name__ == '__main__':
    main()
