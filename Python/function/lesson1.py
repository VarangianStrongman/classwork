import random

# st1 = ["Иван", 23 , 111 , 4.5]
# st2 = ["Федор", 20 , 311 , 4]
# st3 = ["Мария", 21 , 311 , 4.7]
# st4 = ["Ваха", 19 , 311 , 3.1]
# st5 = ["Зухра", 23 , 111 , 3.0]
#
# students=[st1,st2,st3,st4,st5]
# print("name\t\tage\t\tgroup\tmark")
# for i in students:
#     for j in i:
#         print(j,end="\t\t")
#     print()
###### КРЕСТИКИ НОЛИКИ ###########################

desk = []
for i in range(3):
    desk.append(["-","-","-"])

# for i in desk:
#     for j in i:
#         print(j,end=" ")
#     print()
count_step=0


# проверка победы
def check_result():
    # проверка по горизонтали
    for i in range(3):
        if desk[i][0]=="-":
            continue
        compare = desk[i][0]
        flag = True
        for j in range(3):
            if compare!=desk[i][j]:
                flag=False
                break
        if flag:
            print("победил", compare)
            return True
    # проверка по вертикали
    for i in range(3):
        if desk[0][i]=="-":
            continue
        compare = desk[0][i]
        flag = True
        for j in range(3):
            if compare!=desk[j][i]:
                flag=False
                break
        if flag:
            print("победил", compare)
            return True
    # проверка диагонали
    if desk[0][0]==desk[1][1]==desk[2][2] and desk[0][0]!="-":
        print("победил ", desk[0][0])
        return True
    if desk[0][2]==desk[1][1]==desk[2][0] and desk[0][2]!="-":
        print("победил ", desk[0][2])
        return True


    # проверка ничьи и заполнения таблицы
    if count_step>=9:
        print("ничья")
        return True
    return False


#вывод игрового поля
def show_desk():
    print("    a b c")

    for i in range(len(desk)):
        print(i+1,"|",end=" ")
        for j in range(len(desk[i])):
            print(desk[i][j],end=" ")
        print()


# ввод данных
def step(symbol):
    global count_step
    while True:
        y=int(input("введите номер строки :"))
        x=int(input("введите номер столбца :"))
        if 0<y<4 and 0<x<4 and desk[y-1][x-1]=="-":
           desk[y-1][x-1]=symbol
           count_step+=1
           break
        print("некорректные данные")


if __name__=="__main__":
    while True:
        show_desk()
        print("ходят крестики")
        step("X")
        if check_result():
           break
        show_desk()
        print("ходят нолики")
        step("0")
        if check_result():
            break
    show_desk()