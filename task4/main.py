"""
Головний модуль для роботи з контактами, який відповіає за введення-виведення 
та керування виконанням відповідних операцій.
"""

from handlers import add_contact, change_contact, show_phone, show_all
from utils import parse_input

def main():
    """
    Головна функція, яка реалізує взаємодію з користувачем через командний інтерфейс.

    Запускає цикл, який чекає вводу команди від користувача та виконує відповідні дії.
    Завершує програму, коли користувач вводить команду "close" або "exit".
    """
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
