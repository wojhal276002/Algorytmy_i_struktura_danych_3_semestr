
def Suma(lista):
    """
    Funkcja odpowiedzialna za zsumowanie wszystkich elementów tablicy n x n

    Parametry:
    lista - list
        lista list, które będziemy sumować

    Output:
        suma tablicy/stosowny komunikat, że tablica nie jest właściwego formatu
    """
    for i in range(1, len(lista)):
        if len(lista[i]) != len(lista[0]):
            return ValueError("zły rozmiar tablicy, listy wewnątrz listy głównej powinny mieć taką samą długość")
    return sum(sum(listy) for listy in lista)

if __name__=="__main__":
    lista = [[1, 1, 2], [1, 1], [1, 1, 1]]
    print(Suma(lista))

