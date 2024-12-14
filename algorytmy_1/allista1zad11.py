import random

def wielomian(punkt, wspolczynniki=1):
    """
    Funkcja odpowiedzialna za wyliczenie losowo wygenerowanego wielomianu w punkcie algorytmem klasy O(n^2)

    Parametry:
    punkt - float
        punkt dla którego ma być wyliczona wartość wielomianu
    wspolczynniki - int
        liczba współczynników losowego wielomianu
    Output:
    Wartość wielomianu w punkcie

    """
    if wspolczynniki < 1 or type(wspolczynniki) != int:
        raise ValueError("Liczba współczynników musi być liczbą naturalną >= 1")
    lista_a = [random.randint(-10,10) for n in range(wspolczynniki)]
    print(f"Oto współczynniki twojego wielomianu: {lista_a}")
    suma = 0
    od_tylu = lista_a[::-1]
    for i in range(len(lista_a)):
        for j in range(len(lista_a)):
                if i == j:
                    suma += od_tylu[i]*punkt**j
    return(f"Funkcja w punkcie x={punkt} przyjmuje wartość {suma}")

print(wielomian(2,5))
print(wielomian(0,5))