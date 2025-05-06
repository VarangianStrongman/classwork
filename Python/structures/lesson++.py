import random

len_array1 = int(input("введи длину первого списка :"))
len_array2 = int(input("введи длину второго списка :"))
array1 = []
array2 = []
array3 = []
flag = True
for i in range(len_array1):
    num = random.randint(0, 10)
    array1.append(num)
for i in range(len_array2):
    num = random.randint(0, 10)
    array2.append(num)
# for i_1 in range(len_array1):
#     for i_2 in range(len_array2):
#         if array1[i_1] == array2[i_2]:
#             flag = False
#             for i_3 in range(len(array3)):
#                 if array3[i_3] == array1[i_1]:
#                     flag = True
#                     break
#             if flag == False:
#                 array3.append(array1[i_1])
#                 break
for i1 in range(len_array1):
    flag = False
    flag2 = False
    for i2 in range(i1+1,len_array1):
        if array1[i1] == array1[i2]:
            flag = True
            break
    for i3 in range(len_array2):
        if array1[i1] == array2[i3]:
            flag2 = True
            break
    if flag==False and flag2==False:
        array3.append(array1[i1])

print(array1)
print(array2)
print(array3)
#доделдать. так чтобы в третий массив выводились все числа которые уникальны
#(не повторяются ни у себя ни в соседнем массиве)