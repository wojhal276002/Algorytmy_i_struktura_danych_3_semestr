import matplotlib.pyplot as plt
import time
from allista1zad20 import generatoinator

def appendowanie(lista_pocz, lista):
    """
    Funkcja do metody wielokrotnego appendu

    Parametry:
    lista_pocz - list
        lista początkowa
    lista - list
        lista, o którą będziemy listę początkową wydłużać

    Output:
    lista_pocz - list
        wydłużona lista
    """
    for i in lista:
        lista_pocz.append(i)
    return lista_pocz

def extendowanie(lista_pocz, lista):
    """
        Funkcja do metody wielokrotnego extend

        Parametry:
        lista_pocz - list
            lista początkowa
        lista - list
            lista, o którą będziemy listę początkową wydłużać

        Output:
        lista_pocz - list
            wydłużona lista
        """
    lista_pocz.extend(lista)
    return lista_pocz

def czasomierzator(func, odstep, elem, num, start, stop):
    """
        Funkcja odpowiedzialna za zmierzenie czasów metody jednej z funkcji na wydłużanie list o różne długści tyc list

        Parametry:
        func - function
            funkcja, dla której będziemy mierzyć czas
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
            lista z czasami, w jakich wykonuje się program dla różnych długości list

        """
    lista_czasow = []
    lista_pocz = generatoinator(elem,start,stop)
    for i in range(0,odstep*10,odstep):
        czas = 0
        lista = []
        for j in range(elem+i):
            lista.append(1)
        for n in range(num):
            start = time.time()
            func(lista_pocz,lista)
            end = time.time()
            czas += end - start
            lista_pocz = lista_pocz[0:elem]
        lista_czasow.append(czas / num)
    return lista_czasow

czas1 = czasomierzator(appendowanie, 1000, 1000, 150, 1, 1)
czas2 = czasomierzator(extendowanie, 1000, 1000, 150, 1, 1)


skala = range(0, 10000, 1000)

plt.plot(skala, czas1, "bo", label="append")
plt.plot(skala, czas2, "ro", label="extend")
plt.title("Porównanie długości wykonywania metody extend i wielokrotnego append od czasu ", size=10)
plt.xlabel("Długość łączna listy")
plt.ylabel("Czas")
plt.legend()
plt.show()

