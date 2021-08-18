# Усовершенствовать программу «Банковский депозит».
# Третьим аргументом в функцию должна передаваться фиксированная ежемесячная сумма пополнения вклада.
# Необходимо в главной функции реализовать вложенную функцию подсчета процентов для пополняемой суммы.
# Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего.
# Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев.
# Вложенная функция возвращает сумму дополнительно внесенных средств (с процентами),
# а главная функция — общую сумму по вкладу на конец периода.

begin_sum = 10001
period_deposit = 6
addition = 1000


def bank_deposit(begin_sum: int, period_deposit: int, addition: int) -> (int, int):
    dct = {'begin_sum': None,
           'end_sum': None,
           '6': None,
           '12': None,
           '24': None
           }

    def end_sum(start_sum: int, d: dict, period_dep: int) -> int:
        return start_sum * d[f'{period_dep}'] + start_sum + addition_in_all_time()

    def addition_in_all_time():
        dop = addition * dct[f'{period_deposit}'] * (period_deposit - 2)
        return dop

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

    addition_in_all_time()

    return dct['end_sum'], addition_in_all_time()


print(bank_deposit(begin_sum, period_deposit, addition))
