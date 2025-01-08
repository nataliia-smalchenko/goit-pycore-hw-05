"""Модуль містить рекурсивну функцію для обчислення чисел фібоначчі та зразок її використання."""

def caching_fibonacci():
    """Зовнішня функція для збереження словника зі знайденими числами фібоначчі."""
    cache={}

    def fibonacci(n: int):
        """
        Рекурсивна функція для знаходження чисел фібоначчі з використанням закешованих значень.

        Аргументи:
            n (int): номер числа фібоначчі для пошуку.

        Повертає:
            Знайдене число фібоначчі.
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Отримання функцію fibonacci
fib = caching_fibonacci()

# Тестування коректності роботи функції
assert fib(10) == 55
assert fib(15) == 610

# Використання функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))
print(fib(15))

print(fib.__doc__)
