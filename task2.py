"""
Модуль містить функції для пошуку та генерування дійсних чисел у тексті
та підрахунку їх суми.
"""

import re

def generator_numbers(text: str):
    """
    Генерує всі дійсні числа, що містяться у тексті.

    Аргументи:
        text (str): Текст для аналізу.

    Повертає:
        Генератор дійсних чисел.
    """
    pattern = r'\b\d+(\.\d+)?\b'

    for match in re.finditer(pattern, text):
        yield float(match.group(0))


def sum_profit(text: str, func) -> float:
    """
    Обчислює суму прибутку за допомогою функції-генератора.

    Аргументи:
        text (str): Текст для аналізу.
        func (function): Функція-генератор для знаходження чисел.

    Повертає:
        float: Загальна сума прибутку.
    """
    return sum(func(text))


# Обчислюємо загальний прибуток
my_text = "У нас є доходи 1500.5, 2000 та 3000.75 з різних джерел."

# Обчислюємо загальний прибуток
total_profit = sum_profit(my_text, generator_numbers)

print(f"Загальний прибуток: {total_profit}")
