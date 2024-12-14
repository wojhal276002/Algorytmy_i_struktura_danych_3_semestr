from scipy.optimize import curve_fit
from allista1zad200 import czasomierzator
import matplotlib.pyplot as plt

def example1(S):
    n = len(S)
    total = 0
    for j in range(n):
       total += S[j]
    return total
czas1 = czasomierzator(example1, 50, 100, 100, 1, 100)
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.set_figheight(5)
fig.set_figwidth(12)
skala1 = range(100, 5001, 100)
def func1(x, a, b):
    """
    Wzór funkcji liniowej do dopasowania metodą curve_fit

    """
    return a*x + b
popt, pcov = curve_fit(func1, skala1, czas1)
ax1.plot(skala1, czas1, "bo", label="example1")
ax2.set_title("Eksperymentalna złożoność obliczeniowa funkcji example1", size=10)
ax1.set_xlabel("Długość ciągu")
ax1.set_ylabel("Czas")
ax1.legend()
ax2.loglog(skala1, czas1, label="example1")
ax2.loglog(skala1, func1(skala1, *popt), label="O(n)")
ax2.set_title("Eksperymentalna złożoność obliczeniowa funkcji example1 (skala log-log)", size=10)
ax2.set_xlabel("Długość ciągu")
ax2.set_ylabel("Czas")
ax2.legend()
plt.show()

