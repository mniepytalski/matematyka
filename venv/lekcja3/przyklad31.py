
# to jsst bok naszego kwadratu
bok = 1
obwod = 0

def obwodKwadratu(bok):
    wynik = 4 * bok
    print('obwod kwadratu dla boku {} to {}'.format(bok, wynik))
    return wynik

while obwod < 3333:
    wynik = obwodKwadratu(bok)

    if obwodKwadratu(bok + 1) > 3333:
        break
    else:
        bok = bok + 1

print('wynik')
print(bok)




