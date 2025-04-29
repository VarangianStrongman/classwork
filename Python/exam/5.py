import random
game =  True
winc = 0
winp = 0
while game :
    print("кидай кости")
    gamer1 = random.randint(1, 6)
    gamer2 = random.randint(1, 6)
    comp1 = random.randint(1, 6)
    comp2 = random.randint(1, 6)
    print(f'ты кинул {gamer1} и {gamer2} а комп кинул {comp1} и {comp2}')
    if gamer1 == gamer2 :
        gamer1 *= 2
        gamer2 *= 2
    if comp1 == comp2 :
        comp1 *= 2
        comp2 *= 2
    if gamer1+gamer2 > comp1+comp2:
        print("ты победил")
        winp+=1
    else:
        print("ты проиграл")
        winc+=1
    if winc==3 or winp ==3:
        game = False