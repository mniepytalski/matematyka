
# to jsst bok naszego kwadratu
bok = 1
obwod = 0

while obwod < 3333:
    wynik = 4 * bok

    if 4 * (bok + 1) > 3333:
        break
    else:
        bok = bok + 1

print('wynik')
print(bok)
