"""
 Два натуральных числа называют дружественными, если каждое из них
равно сумме всех делителей другого, кроме самого этого числа. Найти все
пары дружественных чисел, лежащих в диапазоне от 200 до 300. [02-3.2-HL02]
"""
for n in range(200, 301):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    if s > n:
        result = 0
        for i in range(1, s):
            if s % i == 0:
                result += i
        if result == n:
            print(n, s)
