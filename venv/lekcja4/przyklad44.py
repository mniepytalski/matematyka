
import matplotlib.pyplot as plt
import math

# x-axis values
x = []
# y-axis values
y = []

liczba = -500

for i in range(1000):
    x.append(liczba)
    wynik = liczba ** 3 * 10*math.sin(liczba/10)
    y.append( wynik )
    liczba = liczba + 1


# plotting points as a scatter plot
plt.plot(x, y )

# x-axis label
plt.xlabel('x - axis')
# frequency label
plt.ylabel('y - axis')
# plot title
plt.title('Wykres Michała')
# showing legend
plt.legend()

# function to show the plot
plt.show()