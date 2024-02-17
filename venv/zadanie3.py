# liczby do sprawdzenia
#liczby = [630, 822, 1240, 762, 5300, 54, 987120, 1110, 40, 104729, 10201, 20099, 39601, 196436880]
# liczby = [26^2, 26 * 26, 26]
liczby = [241]

# liczby pierwsze do 200
#dzielniki = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
#             107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

dzielniki = [2, 3, 5, 7, 11, 13, 17, 19]

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


