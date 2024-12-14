import random

def generatoinator(elem, start, stop):
    """
    Funkcja odpowiedzialna za wygenerowanie losowego ciągu liczb całkowitych danej długości

    Parametry:
    elem - int
        liczba elementów w ciągu
    start - float
        najmniejsza liczba, która może się pojawić w ciągu
    stop - float
        największa liczba, która może się pojawić w ciągu
    Output:
    lista - list
        ciąg losowych elementów

    """
    lista = [random.randint(start, stop) for n in range(elem)]
    return lista
