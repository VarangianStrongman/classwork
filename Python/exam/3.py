import random
a = int(input("введи первое число :"))
b = int(input("введи второе число :"))
if a>b:
    a,b = b,a
num = int(input(f"введи число в диапазоне от {a} до {b}"))
if num>=a and num<=b:
    game = True
    n=0
else:
    game = False
    print("ошибка ввода!")
while game:
    comp = random.randint(a, b)
    print(comp)
    n+=1
    print(n)
    if comp == num:
        game = False