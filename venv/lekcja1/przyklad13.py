x = 3
y = 10

print(x/y)

n = 0
while n < 160:
    n = n + 1

    wynik = x // y
    reszta = x % y

    x = reszta * 10
    print(wynik, end="")
    if n == 1:
        print('.', end="")
#    print('wynik:{} reszta:{} test:{}'.format(wynik, reszta, x/y))