# numbers=[111,222,333,444,555,666]
# for i in range(len(numbers)):
#     if numbers[i]%2 == 0:
#         print(numbers[i])

# import random
# numbers=[111,222,333,444,555,666,333]
# n=int(input("введи сколько раз"))
# numbers2=[]
# for i in range(n):
#     num = random.randint(0,len(numbers)-1)
#     # print(numbers[num])
#     numbers2.append(numbers[num])
# print(numbers2)


# numbers=[111,222,333,444,555,666]
# for i in range(len(numbers)-1,-1,-1):
#     print(numbers[i])

import random

lenth = int(input("введи длину списка :"))
numbers = []
for i in range(lenth):
    num = random.randint(-100, 100)
    numbers.append(num)
print(numbers)
sumotr = 0
sumchet = 0
sumnechet = 0
proizkr3 = 1
min = numbers[0]
max = numbers[0]
index_min = 0
index_max = 0
first = 0
last = 0
for i in range(len(numbers)):
    if numbers[i] > 0 and first == 0:
        first = i
    if numbers[i] > 0 and first != 0:
        last = i
    if numbers[i] < 0: sumotr += numbers[i]
    if numbers[i] % 2 == 0:
        sumchet += numbers[i]
    else:
        sumnechet += numbers[i]
    if i % 3 == 0:
        proizkr3 *= numbers[i]
    if numbers[i] < min:
        min = numbers[i]
        index_min = i

    if numbers[i] > max:
        max = numbers[i]
        index_max = i
proizminmax = min * max
print(sumotr, sumchet, sumnechet, proizkr3, proizminmax, first, last)
sumfl = 0
for i in range(first, last + 1):
    print(numbers[i], end=" ")
    sumfl += numbers[i]
print(sumfl)
if index_min>index_max:
    index_min,index_max = index_max,index_min
min_max_proizv=1
for i in range(index_min,index_max+1):
    min_max_proizv*=numbers[i]
    print(numbers[i], end=" ")
print(min_max_proizv)
