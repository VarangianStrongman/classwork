a = int(input("введи первое число :"))
b = int(input("введи второе число :"))
if a>b:
    a,b = b,a
n=0
sum = 0
if a%3 != 0:
    a = a + (3 - a%3)
for i in range(a,b+1,3):
    sum +=i
    n+=1
print(f'{sum/n}')
