"""Модуль містить функції для обробки роботи з контактами"""

from tabulate import tabulate
from utils import input_error

@input_error
def add_contact(args, contacts):
    """
    Додає новий контакт до списку контактів.

    Аргументи:
        args (list): Список з двох елементів: ім'я та номер телефону.
        contacts (dict): Словник контактів, де ключем є ім'я, а значенням - номер телефону.

    Повертає:
        str: Повідомлення про успішне додавання контакту.

    Викидає:
        ValueError: Якщо не надано ім'я або номер телефону, або контакт з таким ім'ям вже існує.
    """
    if len(args) < 2:
        raise ValueError("You did not provide a name or phone number.")
    elif len(args) > 2:
        raise ValueError("You have specified more arguments than required.\n" \
                         "The command takes 2 arguments: name and phone number.")

    name, phone = args
    if name in contacts:
        raise ValueError(f"Contact with name {name} already added.")

    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    """
    Змінює існуючий контакт у списку контактів.

    Аргументи:
        args (list): Список з двох елементів: ім'я та новий номер телефону.
        contacts (dict): Словник контактів, де ключем є ім'я, а значенням - номер телефону.

    Повертає:
        str: Повідомлення про успішне оновлення контакту.

    Викидає:
        ValueError: Якщо не надано ім'я або номер телефону, або контакт з таким ім'ям не знайдений.
    """
    if len(args) < 2:
        raise ValueError("You did not provide a name or phone number.")
    elif len(args) > 2:
        raise ValueError("You have specified more arguments than required.\n" \
                         "The command takes 2 arguments: name and phone number.")

    name, phone = args
    if name not in contacts:
        raise ValueError(f"There is no contact with name {name}.")

    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    """
    Показує номер телефону для вказаного контакту.

    Аргументи:
        args (list): Список з одним елементом - ім'я контакту.
        contacts (dict): Словник контактів, де ключем є ім'я, а значенням - номер телефону.

    Повертає:
        str: Номер телефону для зазначеного контакту.

    Викидає:
        ValueError: Якщо не надано ім'я або контакт з таким ім'ям не знайдений.
    """
    if len(args) < 1:
        raise ValueError("You did not provide a name.")
    elif len(args) > 1:
        raise ValueError("You have specified more arguments than required.\n" \
                         "The command takes only 1 argument: name.")

    name = args[0]
    if name not in contacts:
        raise ValueError(f"There is no contact with name {name}.")

    return contacts[name]

@input_error
def show_all(contacts):
    """
    Показує всі контакти в списку.

    Аргументи:
        contacts (dict): Словник контактів, де ключем є ім'я, а значенням - номер телефону.

    Повертає:
        str: Створену таблицю з усіма контактами у форматі "Name | Phone".
    """
    contacts_list = [(name, contacts[name]) for name in contacts ]
    return tabulate(contacts_list, headers=("Name", "Phone"), tablefmt="fancy_grid")
