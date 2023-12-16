
from datetime import datetime,timedelta
import re

email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

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
    
    # Task 1 and 3
    def add_contact(self):
        
        inputs = input('Enter name: ')
        record = Record(inputs)

        while True:
            inputs = input('Enter phone number: ')
            if not inputs or not inputs.isdigit():
                print("Invalid phone number. Please provide a valid numeric phone number.")
            else:
                record.phones.append(inputs)
                break

        while True:
            inputs = input('Enter maill: ')
            if not inputs or not re.match(email_regex, inputs):
                print("Invalid email. Please provide a valid email address.")
            else:
                record.mails.append(inputs)
                break

        while True:
            inputs = input('Enter birthday (dd.mm.yyyy): ')
            try:
                record.birthday = Birthday(inputs)
                break
            except ValueError:
                print("Incorrect birthday date format. Use the format dd.mm.yyyy.")      

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
        print("\nEnter the command (For a list of available commands, enter 'help'):")
        command = input("> ").lower()

        if command == 'help':
            print("Available commands: exit, add_contact, birthday_day")
        elif command == 'add_contact':
            assistant.add_contact()
        elif command == "birthday_day":
            assistant.get_birthdays()
        elif command == 'exit':
            print("Goodbye!")
            break

        else:
            print("Unknown command. Type 'help' for a list of available commands")

if __name__ == "__main__":
    main()