import numpy
import random

print("введите количество элементов массива:")
n = int(input())
condition = n>=2 and n<100
if condition:
    arr = [0]*n
    arr = list(map(lambda item: random.randint(0,100),arr))
    print(f"original array: {arr}")
    print(f"reversed array: {list(reversed(arr))}")
else:
    print("число элементов массива должно быть менее ста и больше либо равно 2")