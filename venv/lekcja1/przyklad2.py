dzielnik = 3
liczba = 0
while liczba < 10:
    liczba = liczba + 1
    wynik = liczba / dzielnik
    reszta = liczba % dzielnik
    print('----------')
    print('liczba:{} wynik:{} reszta:{}'.format(liczba, wynik, reszta))
    if reszta == 0:
        print('liczba podzielna przez {}'.format(dzielnik))
    else:
        print('liczba niepodzielna przez {}'.format(dzielnik))