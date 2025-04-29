size = int(input("введи сторону:"))
if size%2 == 0:
    size+=1
for i in range(size):
    for j in range(size):
        if i == 0 or i == size-1 or i == size//2:
            print("*", end= " ")
        elif  j == 0 or j == size-1 or j == size//2:
            print("*", end= " ")
        else:
            print(" ", end= " ")

    print("")