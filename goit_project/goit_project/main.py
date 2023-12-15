#test comment

class PersonalAssistant:
    def __init__(self):
        self.contacts = []
        self.notes = []

    def task_1(self):
        1+1

    def task_2(self):
        2+2

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
        elif command == 'exit':
            print("До побачення!")
            break
        else:
            print("Невідома команда. Введіть 'help' для списку доступних команд.")

if __name__ == "__main__":
    main()