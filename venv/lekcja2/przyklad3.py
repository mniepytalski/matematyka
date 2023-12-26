liczba = 7
licznik = 0
wynik = 1

while wynik < 1000:
    if (wynik * liczba) > 1000:
        print('wynik wiekszy od 1000')
        break
    else:
        wynik = wynik * liczba
        licznik = licznik + 1

print('liczba:{} wynik:{} licznik:{}'.format(liczba, wynik, licznik))

