liczba = 0
while liczba < 10:
    liczba = liczba + 1
    wynik = liczba / 2
    reszta = liczba % 2
    print('liczba:{} wynik:{} reszta:{}'.format(liczba, wynik, reszta))
    if reszta == 0:
        print('liczba parzysta')
    else:
        print('liczba nieparzysta')