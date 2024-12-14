import timeit
from allista1zad20 import generatoinator

def czasomierzator(func, punkty, odstep, elem, start, stop, ex4=False):
    """
    Funkcja odpowiedzialna za zmierzenie kolejnych czasów wykonania funkcji tyle razy, ile użytkownik sobie zażyczy

    Parametry:
    func - function
        funkcja, na której działamy
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
    ex4 - bool
        sprecyzowanie czy omawianą funkcją jest example4; jeśli tak to dostosowanie funkcji do jej specyfikacji
    Output:
    lista_czasow - list
        lista kolejnych zarejestrowanych czasów wykonywania funkcji podanej w argumentach

    """
    lista_czasow = []
    if ex4 == True:
        for n in range(punkty):
            lista_czasow.append(timeit.timeit(lambda:func(generatoinator(elem,start,stop), generatoinator(elem,start,stop)), number=150))
            elem+=odstep
    else:
        for n in range(punkty):
            lista_czasow.append(timeit.timeit(lambda:func(generatoinator(elem,start,stop)), number=150))
            elem+=odstep
    return lista_czasow
