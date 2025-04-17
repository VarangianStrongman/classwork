import random
game = True
winp = 0
winc = 0
while game:
    comp = random.randint(1,3)
    player = input("загадай камень, ножницы или бумага :")
    if player == "камень" and comp == 1:
        print("камень-камень. ничья.")
    elif player == "камень" and comp == 2:
        print("камень-ножницы. ты победил раунд!")
        winp += 1
    elif player == "камень" and comp == 3:
        print("камень-бумага. ты проиграл раунд!")
        winc += 1
    elif player == "ножницы" and comp == 1:
        print("ножницы-камень. ты проиграл раунд!")
        winc += 1
    elif player == "ножницы" and comp == 2:
        print("ножницы-ножницы. ничья.")
    elif player == "ножницы" and comp == 3:
        print("ножницы-бумага. ты победил раунд!")
        winp += 1
    elif player == "бумага" and comp == 1:
        print("бумага-камень. ты победил раунд!")
        winp += 1
    elif player == "бумага" and comp == 2:
        print("бумага-ножницы. ты проиграл раунд!")
        winc += 1
    elif player == "бумага" and comp == 3:
        print("бумага-бумага. ничья.")
    else:
        print("ошибка ввода. ты проиграл раунд!")
        winc += 1
    print(f'счет - игрок: {winp} компьютер: {winc}')
    if winp == 3:
        print("ТЫ ПОБЕДИЛ МАТЧ!")
        player = input("сыграем еще раз? :")
        winp = 0
        winc = 0
        if player != "да":
            game = False
    if winc == 3:
        print("ТЫ ПРОИГРАЛ МАТЧ!")
        player = input("сыграем еще раз? :")
        winp = 0
        winc = 0
        if player != "да":
            game = False




