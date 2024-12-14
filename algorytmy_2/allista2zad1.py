def skrajnosc(list, max):
    """

    Funkcja odpowiedzialna za znalezienie największego elementu w podanej sekwencji

    Parametry:
    list - list
        sekwencja
    max - float
        element, który w danym momencie rekurencji jest największy
    Output:
    max - float
        zwracany po przeanalizowaniu wszystkich elementów największy element sekwencji

    """
    if len(list) > 1:
        if max < list[1]:
            max = list[1]
        else:
            pass
        return skrajnosc(list[1:], max)
    else:
        if max < list[0]:
            max = list[0]
        return max

if __name__=="__main__":
    list = [71, 34, 54, 12, 32,8, 19,60,99]
    print(skrajnosc(list, list[0]))

