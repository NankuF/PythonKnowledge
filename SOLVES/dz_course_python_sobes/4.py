# Написать программу «Банковский депозит».
# Она должна состоять из функции и ее вызова с аргументами.
# Клиент банка делает депозит на определенный срок.
# В зависимости от суммы и срока вклада определяется процентная ставка:
# 1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых).
# 10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 года – 6.5 % годовых).
# 100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых).
# Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада.
# Каждый из трех банковских продуктов должен быть представлен в виде словаря с ключами (begin_sum, end_sum, 6, 12, 24).
# Ключам соответствуют значения начала и конца диапазона суммы вклада и значения процентной ставки для каждого срока.
# В функции необходимо проверять принадлежность суммы вклада к одному из диапазонов
# и выполнять расчет по нужной процентной ставке.
# Функция возвращает сумму вклада на конец срока.

summa = 100010
time = 24


def bank_deposit(begin_sum: int, period_deposit: int) -> int:
    dct = {'begin_sum': None,
           'end_sum': None,
           '6': None,
           '12': None,
           '24': None
           }

    # end_sum = lambda begin_sum: begin_sum * dct[f'{period_deposit}'] + begin_sum
    def end_sum(start_sum: int, d: dict, period_dep: int) -> int:
        return start_sum * d[f'{period_dep}'] + start_sum

    if 1000 <= begin_sum <= 10000:
        if period_deposit == 6:
            dct[f'{period_deposit}'] = 0.05
        elif period_deposit == 12:
            dct[f'{period_deposit}'] = 0.06
        elif period_deposit == 24:
            dct[f'{period_deposit}'] = 0.05
        dct['begin_sum'] = begin_sum
        dct['end_sum'] = end_sum(begin_sum, dct, period_deposit)

    elif 10000 < begin_sum <= 100_000:
        if period_deposit == 6:
            dct[f'{period_deposit}'] = 0.06
        elif period_deposit == 12:
            dct[f'{period_deposit}'] = 0.07
        elif period_deposit == 24:
            dct[f'{period_deposit}'] = 0.65
        dct['begin_sum'] = begin_sum
        dct['end_sum'] = end_sum(begin_sum, dct, period_deposit)

    elif 100_000 < begin_sum <= 1_000_000:
        if period_deposit == 6:
            dct[f'{period_deposit}'] = 0.07
        elif period_deposit == 12:
            dct[f'{period_deposit}'] = 0.08
        elif period_deposit == 24:
            dct[f'{period_deposit}'] = 0.75
        dct['begin_sum'] = begin_sum
        dct['end_sum'] = end_sum(begin_sum, dct, period_deposit)

    return dct['end_sum']


print(bank_deposit(summa, time))
