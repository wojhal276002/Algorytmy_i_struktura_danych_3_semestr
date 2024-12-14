from scipy.optimize import curve_fit
from allista1zad200 import czasomierzator
import matplotlib.pyplot as plt

def example4(A, B):
    n = len(A)
    count = 0
    for i in range(n):
        total = 0
        for j in range(n):
           for k in range(1+j):
               total += A[k]
        if B[i] == total:
           count += 1
    return count

czas4 = czasomierzator(example4, 50, 1, 1, 1, 100, ex4=True)
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.set_figheight(5)
fig.set_figwidth(12)
skala4 = range(1, 51, 1)
def func4(x, a, b, c, d):
    """
    Wzór funkcji do 3 potęgi do dopasowania metodą curve_fit

    """
    return a*x*x*x + b*x*x + c*x + d
popt, pcov = curve_fit(func4, skala4, czas4)
ax1.plot(skala4, czas4, "bo", label="example4")
ax1.set_title("Eksperymentalna złożoność obliczeniowa funkcji example4", size=10)
ax1.set_xlabel("Długość ciągu")
ax1.set_ylabel("Czas")
ax1.legend()
ax2.loglog(skala4, czas4, label="example4")
ax2.loglog(skala4, func4(skala4, *popt), label="O(n^3)")
ax2.set_title("Eksperymentalna złożoność obliczeniowa funkcji example4 (skala log-log)", size=10)
ax2.set_xlabel("Długość ciągu")
ax2.set_ylabel("Czas")
ax2.legend()
plt.show()