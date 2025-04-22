# hi = int(input("введи высоту :"))
# wi = int(input("введи ширину :"))
# print("* " * wi)
# for i in range(hi-2):
#     print("*"+("  " *(wi-2)) + " *")
# print("* " * wi)

# size = int(input("введи сторону :"))
#
# for i in range(1,size+1):
#     print("* " * i)

# size = int(input("введи сторону :"))
#
# for i in range(size,0,-1):
#     print("* " * i)

# size = int(input("введи сторону :"))
#
# for i in range(size, -1, -1):
#     print("  " * i + "* "* (size-i))
#
# size = int(input("введи сторону :"))
#
# for i in range(0, size):
#     print("  " * i + "* " * (size - i))

# size = int(input("введи сторону :"))
#
# for i in range(size, -1, -2):
#     print("* "*((size - i)//2) + "  "*i + "* "*((size - i)//2))
# a = 0
# if size%2:
#     a = 3
# else:
#     a = 2
# for i in range(a, size+1, 2):
#     print("* "*((size - i)//2) + "  "*i + "* "*((size - i)//2))


# size = int(input("введи сторону :"))
# for i in range(0,size,2):
#     for j in range(i//2):
#         print(" ", end=" ")
#     for j in range(i,size):
#         print("*", end=" ")
#     for j in range(i//2):
#         print(" ", end=" ")
#     print(" ")

# size = int(input("введи сторону :"))
# count = 1
# for i in range(size):
#     for j in range(size):
#         print(count, end= "\t")
#         count+=1
#     print()

# size = int(input("введи сторону :"))
# count = "*"
# for i in range(size):
#     for j in range(size):
#         print(count, end= " ")
#         if count == "*":
#             count = "-"
#         else:
#             count = "*"
#     if count == "*":
#         count = "-"
#     else:
#         count = "*"
#     print()

num = int(input("введи число :"))
n = int(input("введи степень :"))
a=1
for i in range(n):
    a*=num
print(a)
