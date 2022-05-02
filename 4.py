import random

def main():
    n = int(input("введите размер массива: "))
    x = int(input("введите верхнюю границу массива X: "))
    y = int(input("введите нижнюю границу массива Y: "))
    a = [0]*n
    a = list(map(lambda item: getRandNumber(x,y), a))
    print(f"сгенерированный массив: {a}")
    summa = sum(a)
    print(f"сумма элементов массива: {summa}")
    print(f"среднее арифметическое элементов массива: {round(float(summa)/n, 2)}")

def getRandNumber(x,y):
    if(random.random()>0.5):
        return round(random.random()*(y-x)+x)
    else:
        return round(-random.random()*(y-x)-x)

main()
