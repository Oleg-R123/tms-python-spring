"""
Получить на ввод количество рублей и копеек и вывести в правильной форме.
"""
a = int(input('Введите количество рублей:'))
b = int(input('Введите количество копеек:'))
if b >= 100:
    c = a + b // 100
    d = b % 100
    print(c, 'руб.', d, 'коп.')
else:
    print(a, 'руб.', b, 'коп.')
