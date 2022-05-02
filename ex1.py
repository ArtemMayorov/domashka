import random

n = int(input("введите размер массива: "))
x = int(input("введите порог X: "))
a = [0]*n
a = list(map(lambda item: random.randint(0,100),a))
print(f"сгенерированный массив: {a}")
res = [z for z, w in enumerate(a) if w > x]
print(f"индексы элементов массива, большие, чем {x}: {res}")
