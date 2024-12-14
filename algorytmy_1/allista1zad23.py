from scipy.optimize import curve_fit
from allista1zad200 import czasomierzator
import matplotlib.pyplot as plt

def example3(S):
    """Return the sum of the prex sums of sequence S."""
    n = len(S)
    total = 0
    for j in range(n):
       for k in range(1+j):
           total += S[k]
    return total

czas3 = czasomierzator(example3, 50, 1, 1, 1, 100)
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.set_figheight(5)
fig.set_figwidth(12)
skala3 = range(1, 51, 1)
def func3(x, a, b, c):
    """
    Wzór funkcji kwadratowej do dopasowania metodą curve_fit

    """
    return a*x*x + b*x + c
popt, pcov = curve_fit(func3, skala3, czas3)
ax1.plot(skala3, czas3, "bo", label="example3")
ax1.set_title("Eksperymentalna złożoność obliczeniowa funkcji example3", size=10)
ax1.set_xlabel("Długość ciągu")
ax1.set_ylabel("Czas")
ax1.legend()
ax2.loglog(skala3, czas3, label="example3")
ax2.loglog(skala3, func3(skala3, *popt), label="O(n^2)")
ax2.set_title("Eksperymentalna złożoność obliczeniowa funkcji example3 (skala log-log)", size=10)
ax2.set_xlabel("Długość ciągu")
ax2.set_ylabel("Czas")
ax2.legend()
plt.show()