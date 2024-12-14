from scipy.optimize import curve_fit
from allista1zad200 import czasomierzator
import matplotlib.pyplot as plt


def example2(S):
    n = len(S)
    total = 0
    for j in range(0, n, 2):
       total += S[j]
    return total
czas2 = czasomierzator(example2, 50, 100, 100, 1, 100)
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.set_figheight(5)
fig.set_figwidth(12)
skala2 = range(100, 5001, 100)
def func2(x, a, b):
    """
    Wzór funkcji liniowej do dopasowania metodą curve_fit

    """
    return a*x + b
popt, pcov = curve_fit(func2, skala2, czas2)
ax1.plot(skala2, czas2, "bo", label="example2")
ax1.set_title("Eksperymentalna złożoność obliczeniowa funkcji example2", size=10)
ax1.set_xlabel("Długość ciągu")
ax1.set_ylabel("Czas")
ax1.legend()
ax2.loglog(skala2, czas2, label="example2")
ax2.loglog(skala2, func2(skala2, *popt), label="O(n)")
ax2.set_title("Eksperymentalna złożoność obliczeniowa funkcji example2 (skala log-log)", size=10)
ax2.set_xlabel("Długość ciągu")
ax2.set_ylabel("Czas")
ax2.legend()
plt.show()