from collections import UserList
from datetime import datetime
import sqlite3

from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table, Column


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
        self.console = Console()
        self.db = sqlite3.connect('notecls/notes.db')
        self.cursor = self.db.cursor()
        super().__init__()
      
      
    def add_note(self):
        record = Note(input('Enter name: '), input('Enter desc: '), input('Enter tag: '))
        dict_record = {'name': record.name, 'desc': record.desc, 'tag': record.tag, 'date': record.date}
        self.data.append(dict_record)
        table = Table(
            Column(header='Name', justify='center'),
            Column(header='Description', justify='center'),
            Column(header='Tag', justify='center'),
            Column(header='Date', justify='center'),
            title='NoteBook')
        table.add_row(dict_record['name'], dict_record['desc'], dict_record['tag'], dict_record['date'])
        self.console.print(table)
        

    def find_note(self):
        if self.data:
            key = Prompt.ask('Введіть параметр', choices=['name', 'desc', 'tag'])
            value = input('Введіть значення: ')
            for note in self.data:
                if value in note[key]:
                    table = Table(
                        Column(header='Name', justify='center'),
                        Column(header='Description', justify='center'),
                        Column(header='Tag', justify='center'),
                        Column(header='Date', justify='center'),
                        title='NoteBook')
                    table.add_row(note['name'], note['desc'], note['tag'], note['date'])
                    self.console.print(table)
                    return note
            self.console.print(f'[red]Нотатки з параметром "{key}" та значенням "{value}" не знайдено.[/]')
        else:
            self.console.print('[bold red]Нотатки пусті[/]')


    def change_note(self):
        while True:
            note = self.find_note()
            if not note:
                continue
            yn = Prompt.ask(f'Цю нотатку ви бажди знайти?', choices=['y','n'])
            if yn == 'y':
                key = Prompt.ask('Введіть параметр який бажаєте змінити', choices=['name', 'desc', 'tag'])
                value = input('Введіть значення: ')
                note[key] = value
                table = Table(
                        Column(header='Name', justify='center'),
                        Column(header='Description', justify='center'),
                        Column(header='Tag', justify='center'),
                        Column(header='Date', justify='center'),
                        title='NoteBook')
                table.add_row(note['name'], note['desc'], note['tag'], note['date'])
                self.console.print(table)
                break


    def delete_note(self):
        while True:
            note = self.find_note()
            if not note:
                continue
            yn = Prompt.ask(f'Цю нотатку ви бажди знайти?', choices=['y','n'])
            if yn == 'y':
                key = Prompt.ask('Введіть параметр', choices=['name', 'desc', 'tag'])
                value = input('Введіть значення: ')
                for note in self.data:
                    if value in note[key]:
                        self.data.remove(note)
                        table = Table(
                                Column(header='Name', justify='center'),
                                Column(header='Description', justify='center'),
                                Column(header='Tag', justify='center'),
                                Column(header='Date', justify='center'),
                                title='NoteBook')
                        table.add_row(note['name'], note['desc'], note['tag'], note['date'])
                        self.console.print(table)
                        break

    
    
    def load_note(self):
        self.cursor.execute(f"DELETE FROM cls_notes")
        self.db.commit()
        for note in self.data:
            self.cursor.execute("INSERT INTO cls_notes (name, desc, tag, date) VALUES (?, ?, ?, ?)",
                (note['name'], note['desc'], note['tag'], note['date']))
        self.db.commit()
        # print('Load')

    def dump_note(self):
        self.cursor.execute("SELECT * FROM cls_notes")
        for note in self.cursor.fetchall():
            dict_note = {'name': note[0], 'desc': note[1], 'tag': note[2], 'date': note[3]}
            self.data.append(dict_note)    
        # print('Dump')

    def bye(self):
        
        print('Good bye!')
        return exit()



def main():
    nbook = NoteBook()
    nbook.dump_note()
    while True:
        try:
            enter = Prompt.ask('[blue]Enter command[/]').lower().strip()
            if enter == 'add-note':
                nbook.add_note()
            elif enter == 'find-note':
                nbook.find_note()
            elif enter == 'change-note':
                nbook.change_note()
            elif enter == 'delete-note':
                nbook.delete_note()
            elif enter in ['close', 'exit', 'good bye']:
                print(nbook.bye())
            else:
                print('Wrong command(')
        finally:
            nbook.load_note()
        
if __name__ == '__main__':
    main()
