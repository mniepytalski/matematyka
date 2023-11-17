from datetime import datetime
import math

start = datetime.now()
current_time = start.strftime("%H:%M:%S")

pierwsze = [2, 3]

liczba = 5

while liczba < 1000000:

    polowa = math.sqrt(liczba)

    sprawdzenie = 1
    for pierwsza in pierwsze:

        if pierwsza > polowa:
            break

        reszta = liczba % pierwsza
        if reszta == 0:
            sprawdzenie = 0
            break

    if sprawdzenie == 1:
        pierwsze.append(liczba)

    liczba += 2

print(pierwsze)

print("Start Time =", current_time)
end = datetime.now()
stop_time = end.strftime("%H:%M:%S")
print("Stop Time =", stop_time)
print("time = ", end - start)
print("find:{} numbers".format(len(pierwsze)))
