liczby = [630, 822, 1240, 762, 5300, 54, 987120, 1110, 40, 104729]

dzielniki = [2, 3, 5, 7, 11, 13, 17]
for liczba in liczby:
    i = 0
    print('---------')
    print("sprawdzamy = {}".format(liczba))
    while i < len(dzielniki):
        dzielnik = dzielniki[i]
        reszta_z_dzielenia = liczba % dzielnik
        if reszta_z_dzielenia == 0:
            print('{} | {}'.format(liczba, dzielnik))
            liczba = liczba / dzielnik
        else:
            i += 1
            if i == len(dzielniki):
                print('{}'.format(liczba))


