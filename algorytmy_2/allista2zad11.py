from scipy.optimize import curve_fit
from allista1zad200 import czasomierzator
import matplotlib.pyplot as plt
from allista2zad1 import skrajnosc

czas = czasomierzator(skrajnosc, 9, 100, 100, -100, 100, skrajnosc=True)
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.set_figheight(5)
fig.set_figwidth(12)
skala = range(100, 901, 100)

def func3(x,a,b,c):
    """
    Wzór funkcji kwadratowej do dopasowania metodą curve_fit

    """
    return a*x*x + b*x + c

popt1, pcov1 = curve_fit(func3, skala, czas)
ax1.plot(skala, czas, "bo", label="sorted")
ax1.plot(skala, func3(skala, *popt1), label="O(n logn)", color="red")
ax1.set_title("Eksperymentalna złożoność obliczeniowa funkcji sorted", size=10)
ax1.set_xlabel("Długość ciągu")
ax1.set_ylabel("Czas")
ax1.legend()
ax2.loglog(skala, czas, label="sorted")
ax2.loglog(skala, func3(skala, *popt1), label="O(n logn)")
ax2.set_title("Eksperymentalna złożoność obliczeniowa funkcji sorted (skala log-log)", size=10)
ax2.set_xlabel("Długość ciągu")
ax2.set_ylabel("Czas")
ax2.legend()
plt.show()

