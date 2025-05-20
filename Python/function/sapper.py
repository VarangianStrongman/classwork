###### САПЕР ###########################
import random

mineFieldSize = int(input("введи размер поля"))
mineNumber = int(input("введи количество мин"))
mineField =[]

#пустое поле создаем
for i in range(mineFieldSize):
    mineField.append([])
    for j in range(mineFieldSize):
        mineField[i].append("-")
# print(mineField)

#минируем
for i in range(mineNumber):
    mineX = random.randint(0,mineFieldSize-1)
    mineY = random.randint(0,mineFieldSize-1)
    mineField[mineX][mineY] = "X"
# print(mineField)

# вывод "заминированного" поля со скрытой миной
def show_MineField():
    for i in range(mineFieldSize):
        for j in range(mineFieldSize):
            if mineField[i][j]=="X":
                print("-",end=" ")
            else:
                print(mineField[i][j],end=" ")
        print()

# разминирование
while True:
    boomX = int(input("введи номер по высоте"))
    boomY = int(input("введи номер по длине"))
    if mineField[boomX][boomY] =="V":
        print("ошибка ввода")
        continue
    elif mineField[boomX][boomY] =="X":
        print("ты подорвался!!!")
        break
    else:
        mineField [boomX][boomY] ="V"
        show_MineField()

