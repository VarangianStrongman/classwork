# stringIncoming = input("введи строку")
# revStrOutput = ''.join(reversed(stringIncoming))
# print(revStrOutput)

# strInc = input("введи строку")
# num = 0
# let = 0
# for i in strInc:
#     if i.isdigit() :
#         num+=1
#     if i.isalnum() :
#         let+=1
# print(f'букв:{let} цифр:{num}')

# strInc = input("введи строку :")
# symSer = input("введите символ для поиска и подсчета :")
# count = 0
# for i in strInc:
#     if i == symSer:
#         count+=1
# print(f'символ {symSer} встречается в строке {count} раз')

# strInc = input("введи строку :")
# symSer = input("введите символ для поиска и подсчета :")
# strInc.count(symSer)
# print(strInc.count(symSer))


strInc = input("введи строку :")
wordSer = input("введите символ для поиска :")
wordNew = input("введите символ для замены :")
print(strInc.replace(wordSer, wordNew))