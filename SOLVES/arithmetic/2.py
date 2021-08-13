# 2. Вывести на экран текущее название дня недели,
# название месяца и свое имя.
# Каждое слово должно быть в отдельной строке.

from datetime import date

WEEKDAY = date(2021, 8, 12).weekday()
MONTH = date.today().timetuple()
NAME = 'VALERIY'


def name_month(s_month: tuple) -> [int, str, int]:
    year = ''
    int_month = ''
    day = ''

    count = 0
    for i in s_month:
        if count == 0:
            # print('year:', i)
            year = i
            count += 1
        elif count == 1:
            # print('int_month:', i)
            int_month = i
            count += 1
        elif count == 2:
            # print('day:', i)
            day = i
            count += 1

    month = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }

    return [year, month[int_month], day]
# print(name_month(MONTH))


def weekday(int_day: int) -> [str]:
    weekday = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    return weekday[int_day]
# print(weekday(WEEKDAY))


def name(variable: str) -> str:
    return variable
# print(name(NAME))


def weekday_month_name(w, m, n):
    weekday1 = w
    name_month1 = m[1]
    name1 = n
    print(weekday1, name_month1, name1, sep='\n')
    # return weekday1, name_month1, name1


weekday_month_name(weekday(WEEKDAY), name_month(MONTH), name(NAME))
