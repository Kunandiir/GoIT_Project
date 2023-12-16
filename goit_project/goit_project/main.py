
from datetime import datetime,timedelta

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

    def task_11(self):
        11+11





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
        elif command == 'exit':
            print("До побачення!")
            break

        else:
            print("Невідома команда. Введіть 'help' для списку доступних команд.")

if __name__ == "__main__":
    main()