import tracemalloc
from allista1zad20 import generatoinator
from allista2zad1 import skrajnosc
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(12000)

def generatoinator_pamieci(func, punkty, odstep, elem, start, stop):
    """
    Funkcja odpowiedzialna za zmierzenie zużycia pamięci przez jakiś program

    Parametry:
    func - function
        funkcja, której zużycie chcemy zmierzyć
    punkty - int
        ile razy funkcja ma zostać wywołana
    odstep - int
        o ile więcej elementów ma być przy kolejnym wykonaniu funkcji
    elem - int
        liczba elementów w ciągu
    start - float
        najmniejsza liczba, która może się pojawić w ciągu
    stop - float
        największa liczba, która może się pojawić w ciągu
    Output:
    (pamiec_now, pamiec_top) - tuple
        krotka zawierająca dane o zużyciu pamięci obecnej oraz najwyższej przez program w odpowiednich listach

    """
    pamiec_now = []
    pamiec_top = []
    for i in range(punkty):
        tracemalloc.start()
        l = generatoinator(elem,start, stop)
        func(l, l[0])
        now, top = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        pamiec_now.append(now)
        pamiec_top.append(top)
        elem += odstep
    return (pamiec_now, pamiec_top)


wynik = generatoinator_pamieci(skrajnosc, 100, 10, 100, 1, 100)
xs = range(100, 1100, 10)
plt.plot(xs, wynik[0], "rD", label="current")
plt.plot(xs, wynik[1], "bD", label="peak")
plt.title("Zależność między długością listy a zużyciem pamięci")
plt.xlabel("Długość ciągu")
plt.ylabel("Zużycie pamięci")
plt.legend()
plt.show()