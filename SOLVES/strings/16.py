# 16. Замените в строке все вхождения 'word' на 'letter'.

s = 'hello word word myunderwordhusbend'


def swap_word_on_letter(s: str):
    new_s = None
    if 'word' in s:
        new_s = s.replace('word', 'letter')

    return new_s


print(swap_word_on_letter(s))
