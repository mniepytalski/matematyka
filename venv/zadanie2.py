x = 55
y = 78

while x < y :
    x += 1
    print('testujemy:{}'.format(x))
    if (x % 3) == 0:
        if ( x % 9) != 0:
            print('{} jest podzielne przez 3 ale nie przez 9'.format(x))