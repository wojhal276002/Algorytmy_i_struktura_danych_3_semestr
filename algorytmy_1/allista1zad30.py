from scipy.optimize import curve_fit
from allista1zad200 import czasomierzator
import matplotlib.pyplot as plt
import numpy as np

czas5 = czasomierzator(sorted, 50, 100, 100, 1, 100)
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.set_figheight(5)
fig.set_figwidth(12)
skala5 = range(100, 5001, 100)

def func3(x,a,b,c):
    """
    Wzór funkcji n*logn do dopasowania metodą curve_fit

    """
    return a*x*np.log(x+b) + c

popt1, pcov1 = curve_fit(func3, skala5, czas5)
ax1.plot(skala5, czas5, "bo", label="sorted")
ax1.plot(skala5, func3(skala5, *popt1), label="O(n logn)", color="red")
ax1.set_title("Eksperymentalna złożoność obliczeniowa funkcji sorted", size=10)
ax1.set_xlabel("Długość ciągu")
ax1.set_ylabel("Czas")
ax1.legend()
ax2.loglog(skala5, czas5, label="sorted")
ax2.loglog(skala5, func3(skala5, *popt1), label="O(n logn)")
ax2.set_title("Eksperymentalna złożoność obliczeniowa funkcji sorted (skala log-log)", size=10)
ax2.set_xlabel("Długość ciągu")
ax2.set_ylabel("Czas")
ax2.legend()
plt.show()