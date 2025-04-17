n = int(input("vvedite: "))
if n <= 0:
    print('oshibka')
f1 = 1
f2 = 1
f = f1 + f2

while f < n:
    if f < n:
        f1 = f2
        f2 = f
        f = f1 + f2
    else:
        print ('oshibka2.0')
        break
if n == f or n == 1:
    print('da')
else:
    print('net')