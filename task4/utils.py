"""Модуль містить додаткові функції"""
from functools import wraps

def parse_input(user_input):
    
    """
    Розбиває введений рядок на команду та аргументи.

    Аргументи:
        user_input (str): Введений рядок з командою та аргументами.

    Повертає:
        tuple: Кортеж, де перший елемент — це команда (стрічка), 
               а решта елементів — це аргументи (список).
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    """
    Декоратор для обробки помилок при виклику функцій.

    Аргументи:
        func (callable): Функція, яку потрібно обгорнути.

    Повертає:
        callable: Обгорнуту функцію з обробкою помилок.
    """
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"Error: {e}"

    return inner
