txt = input('Введите текст: ')

# ******************************

"""Общее количество букв в данном тексте"""

txt_lower = txt.lower()
txt_len = len(txt_lower)
count = 0
list_symbol  = []
list_letter = []
for i in txt_lower:
    if i in " №.1234567890,#():;@ˆ%$*&+_-{}[]?></!'\\\n":
        list_symbol.append(i)
    else:
        list_letter.append(i)
        count += 1
print(f'Общее количество букв в данном тексте: {count}')
print(f'Общее количество других символов в данном тексте: ', txt_len - count)
print(f'Общее количество букв и символов в данном тексте: {txt_len}')

# *****

"""Общее количество слов в данном тексте. Словом, считаются любые символы, разделённые пробелами или переходом на следующую строку."""

txt_new = txt_lower.replace('\n', ' ')
list_new = list(txt_new.split(' '))
list_last = [i for i in list_new if i != '']
print(f'Общее количество слов в данном тексте: {len(list_last)}')

# *****

"""Подсчитать, каких букв и сколько встречается в тексте"""

from collections import Counter
dict_frequency = dict(Counter(list_letter))
# print(f'Частота встречаемости букв: {dict_frequency}')

# *****

"""Вывести их на печать"""

print(f'Частота встречаемости букв:')

"""1) в алфавитном порядке"""
def dict_sorted(k):
    for key, value in k.items():
        return sorted(dict.items(k))
d = dict(dict_sorted(dict_frequency))
print(f'1) в алфавитном порядке: {d}')

"""2) в порядке убывания частоты"""

print(f'2) в порядке убывания частоты: {dict(sorted(d.items(), key=lambda p: p[1], reverse=True))}')

# ******************************
print('THE END')