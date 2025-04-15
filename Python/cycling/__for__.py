#task1
import random

# a = int(input("введите первое число :"))
# b = int(input("введите второе число :"))
# cr = int(input("введите кратность :"))
# if b<a:
#     a,b = b,a
# count = a
# while count<=b:
#     if count%cr==0:
#         print(count)
#         count+=cr
#     else:
#         count+=1

# task2

# a = int(input("введите первое число :"))
# b = int(input("введите второе число :"))
# c = int(input("введите первое_Б число :"))
# d = int(input("введите второе_Б число :"))
# if b<a:
#      a,b = b,a
# if d<c:
#      c,d = d,c
# if a>c:
#     c,d,a,b = a,b,c,d
# # print(a,b,c,d)
# for i in range(c,b)
#     print(i)



# if b%2==1:
#     b-=1
# for i in range (b,a-1,-2):
#     print(i,end=" ")
# count=0
# for i in range(a,b):
#     count+=i
# print(count)

# n = abs(int(input('Введите число: ')))
# count = 0
#
# for i in range(len(str(n))):
#     sum=a%10
#     a=a//10
#     count += 1

# n = int(input("сколько раз? :"))
# sum=0
# for i in range(n):
#     num =int(input("введи число :"))
#     if not num%2:
#         sum+=1
# print(sum)

import random

a = random.randint(10,99)
print(a)
count = 0
num = 0
while count<5:
    count += 1
    num +=1
    n = int(input("угадай число :"))
    if n>a:
        print("слишком большое число")
    elif n<a:
        print("слишком маленькое число")
    elif n==a:
        print(f"угадал за {num} попыток")
        break
    if count == 5:
        ans = input("хочешь сыграть снова :")
        if ans == "да":
            count=0
        elif ans =="нет":
            break
if count==5:
    print("ты проиграл")