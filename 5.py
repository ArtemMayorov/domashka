import random 
def main(): 
    n = int(input("введите размер массива: ")) 
    x,y = int(input("введите верхнюю границу массива X: ")), int(input("введите нижнюю границу массива Y: ")) 
    a = [0]*n
    b = [0]*n
    a = list(map(lambda item: getRandNumber(x,y), a)) 
    b = list(map(lambda item: getRandNumber(x,y), b)) 
    print(f"Первый массив: {a}") 
    print(f"Второй массив: {b}") 
    c = [0]*n
    for index, item in enumerate(c):
        c[index] = a[index] + b[index]
    print(f"Результат: {c}") 
   
   
def getRandNumber(x,y): 
    if(random.random()>0.5): 
        return round(random.random()*(y-x)+x) 
    else: 
        return round(-random.random()*(y-x)-x)
        
        
main()