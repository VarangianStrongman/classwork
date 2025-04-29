age = int(input("введи год рождения :"))
if age >= 1925 and age < 1944:
    print("молчаливое поколение")
elif age >= 1944 and age < 1967:
    print("поколение бэби бумеров")
elif age >= 1967 and age < 1984:
    print("поколение Х")
elif age >= 1984 and age < 2000:
    print("поколение У - миллениалы")
elif age >= 2000 and age < 2011:
    print("поколение Z - зумеры")
elif age >= 2011:
    print("поколение альфа")
else:
    print("ошибка ввода")