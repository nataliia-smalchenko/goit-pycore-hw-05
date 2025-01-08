"""Модуль працює з лог-файлом та виводить статистику по ньому"""

import sys
import re
from collections import Counter
from tabulate import tabulate


def parse_log_line(line: str) -> dict:
    """
    Парсить рядок логу на компоненти: дата, час, рівень логування, повідомлення.

    Аргументи:
        Рядок логу.
    
    Повертає:
        Словник з ключами 'date', 'time', 'level', 'message'.
    """

    log_pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)"
    match = re.match(log_pattern, line)
    if match:
        return {
            'date': match.group(1),
            'time': match.group(2),
            'level': match.group(3),
            'message': match.group(4)
        }
    return None


def load_logs(file_path: str) -> list:
    """
    Завантажує лог-файл та парсить кожен рядок.

    :param file_path: Шлях до файлу.
    :return: Список словників, де кожен елемент містить дані одного логу.
    """
    logs = []
    try:
        with open(file_path, 'r', encoding="utf-8") as f:
            for line in f:
                parsed_line = parse_log_line(line.strip())
                if parsed_line:
                    logs.append(parsed_line)
        return logs

    except FileNotFoundError:
        print(f"Файл за шляхом {file_path} не знайдено.")
        sys.exit(1)
    except PermissionError:
        print("У вас немає прав для доступу до файлу.")
        sys.exit(1)
    except IsADirectoryError:
        print("Вказаний шлях — це директорія, а не файл.")
        sys.exit(1)
    except UnicodeDecodeError:
        print("Помилка декодування під час читання файлу.")
        sys.exit(1)
    except OSError as e:
        print(f"Помилка вводу/виводу: {e}")
        sys.exit(1)


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Фільтрує логи за рівнем логування.

    :param logs: Список логу.
    :param level: Рівень логування (INFO, ERROR, DEBUG, WARNING).
    :return: Список фільтрованих логів.
    """
    return [log for log in logs if log['level'].lower() == level.lower()]


def count_logs_by_level(logs: list) -> dict:
    """
    Підраховує кількість записів для кожного рівня логування.

    :param logs: Список логу.
    :return: Словник з підрахунком рівнів логування.
    """
    level_counts = Counter(log['level'] for log in logs)
    return dict(level_counts)


def display_log_counts(counts: dict):
    """
    Виводить кількість записів за кожним рівнем логування у вигляді таблиці.

    :param counts: Словник з підрахунком рівнів логування.
    """
    headers = ["Рівень логування", "Кількість"]
    print(tabulate(list(counts.items()), headers=headers, tablefmt="presto", stralign="left"))


def display_logs_details(logs: list, level: str):
    """
    Виводить деталі логів для вказаного рівня логування.

    :param logs: Список логу.
    :param level: Рівень логування.
    """
    filtered_logs = filter_logs_by_level(logs, level)
    
    if filtered_logs:
        print(f"\nДеталі логів для рівня '{level}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")
    else:
        print(f"\nНемає логів для рівня '{level}'.")


def main():
    """
    Головна функція, що обробляє аргументи командного рядка та викликає інші функції.
    """
    # Перевірка кількості аргументів командного рядка
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до лог-файлу.")
        sys.exit(1)

    log_file_path = sys.argv[1]

    # Завантаження логів
    logs = load_logs(log_file_path)

    # Підрахунок записів за рівнем
    log_counts = count_logs_by_level(logs)

    # Виведення результатів статистики
    display_log_counts(log_counts)

    # Якщо є другий аргумент, фільтруємо за рівнем
    if len(sys.argv) == 3:
        level_filter = sys.argv[2].upper()
        if level_filter not in ['INFO', 'ERROR', 'DEBUG', 'WARNING']:
            print("Некоректний рівень логування. Доступні рівні: INFO, ERROR, DEBUG, WARNING.")
            sys.exit(1)
        logs = filter_logs_by_level(logs, level_filter)

        # Виведення детальних логів для конкретного рівня
        display_logs_details(logs, level_filter)


if __name__ == "__main__":
    main()
