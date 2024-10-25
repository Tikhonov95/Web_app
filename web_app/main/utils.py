from datetime import date


def is_leap_year(year):
    """Проверяет, является ли год високосным"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Допущение: формат текста "дд.мм.гггг"
def parse_date(date_string: str) -> tuple[int, int, int]:  # принимает дату в виде текста, возвращает 3 числа
    date_strings = date_string.split(".")
    day = int(date_strings[0])
    month = int(date_strings[1])
    year = int(date_strings[2])
    return day, month, year


def get_age(day, month, year):
    """Вычисляет возраст человека, дата рождения которого day/month/year"""

    today = date.today()
    age = today.year - year
    if today.month < month or (today.month == month and today.day < day):
        age -= 1
    return age


def check_date(day, month, year):
    """Проверяет корректность даты. Возвращает True, 
    если дата правильная, False, если найдена ошибка"""

    # Найти max_day
    if month == 2:
        if is_leap_year(year):
            max_day = 29
        else:
            max_day = 28
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:
        max_day = 31

    if all([
        day >= 1,
        day <= max_day,
        month >= 1,
        month <= 12,
        year >= 1,
    ]):
        return True
    else:
        return False