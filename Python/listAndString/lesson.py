# list = [2,3,4]
# print(list)
# list.append(6)
# print(list)
list = []
while True:
    operat = int(input("введите операцию\n 1.добавить значение\n 2.очистить список\n 3.вывести список\n 4.выйти\n 5.количество элементов в списке\n 6.удаление позиции\n 7.удаление элемента\n 8.добавление в позицию\n 9.разворот списка\n 10.сортировка\n :"))
    if operat == 1:
        number = int(input("введи число: "))
        list.append(number)
    elif operat == 2:
        print("список очищен")
        list.clear()
    elif operat == 3:
        print(list)
    elif operat == 4:
        break
    elif operat == 5:
        print(len(list))
    elif operat == 6:
        posNum = int(input("введи номер позиции на удаление :"))
        if posNum > len(list):
            print("ошибка ввода")
        else:
            list.pop(posNum)
    elif operat == 7:
        try:
            elDelNum = int(input("введи элемент на удаление позиции :"))
            list.remove(elDelNum)
        except:
            print("данное значение отсутствует")
    elif operat == 8:
        elIndIns = int(input("введи индекс для вставления"))
        elIns = int(input("введи сам элемент"))
        list.insert(elIndIns, elIns)
    elif operat == 9:
        list.reverse()
    elif operat == 10:
        list.sort(key=None, reverse=False)
    else:
        print("ошибка ввода")


# количество элементов в списке
# удаление с конкретной позиции
# удаление конкретного элемента
# добавление в конкретную позицию
# разворот в обратном порядке и сортировка
