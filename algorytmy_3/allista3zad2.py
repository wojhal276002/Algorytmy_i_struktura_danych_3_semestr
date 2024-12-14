import matplotlib.pyplot as plt
import time
from allista1zad20 import generatoinator

def czasomierzator(odstep, elem, num, start, stop):
    """
    Funkcja odpowiedzialna za zmierzenie czasów metody pop dla różnych wartości indeksów listy złożonej z samych jedynek

    Parametry:
    odstep - int
        co ile ma być indeks
    elem - int
        liczba elementów w liście głównej
    num - int
        liczba powtórzeń wykonania metody dla każdego indeksu
    start - int
        najmniejszy element (tutaj weźmy 1)
    stop - int
        największy element (również 1)

    Output:
    lista_czasow - list
        lista z czasami, w jakich wykonuje się program dla różnych indeksów

    """
    lista_czasow = []
    lista = generatoinator(elem,start,stop)
    for i in range(0,elem,odstep):
        czas = 0
        for n in range(num):
            start = time.time()
            lista.pop(i)
            end = time.time()
            czas += end - start
            lista.append(1) #żeby znowu lista miała tyle samo elementów
        lista_czasow.append(czas / num)
    return lista_czasow

czas = czasomierzator(100000,1000000,150,1,1)

skala = range(0, 1000000, 100000)

plt.plot(skala, czas, "bo", label="pop")
plt.title("Długość wykonywania metody pop w zależności od indeksu listy", size=10)
plt.xlabel("Indeksy listy")
plt.ylabel("Czas")
plt.legend()
plt.show()