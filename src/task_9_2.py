"""
Создать lambda функцию, которая принимает на вход неопределенное
количество именных аргументов и выводит словарь с ключами удвоенной
длины. {‘abc’: 5} -> {‘abcabc’: 5}
"""

print((lambda **kwargs: {i * 2: j for i, j in kwargs.items()})(aale=1, bo=2))
