import random

def wielomian2(punkt, wspolczynniki=1):
    """
        Funkcja odpowiedzialna za wyliczenie losowo wygenerowanego wielomianu w punkcie algorytmem klasy O(n logn)

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
    lista_a = [random.randint(-10, 10) for n in range(wspolczynniki)]
    print(f"Oto współczynniki twojego wielomianu: {lista_a}")
    suma = 0
    od_tylu = lista_a[::-1]
    for i in range(len(lista_a)):
        pol = pow(punkt, i // 2)
        pol = pol * pol
        if i % 2 != 0:
           pol = pol * punkt
        suma += od_tylu[i]*pol
    return (f"Funkcja w punkcie x={punkt} przyjmuje wartość {suma}")

print(wielomian2(2,5))
print(wielomian2(0,5))