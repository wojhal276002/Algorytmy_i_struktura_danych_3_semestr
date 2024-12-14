def mnozenie(a,b,i=0,wynik=0):
    """
    Funkcja odpowedzialna za rekurencyjne mnożenie dwóch liczb
    Parametry:
    a - int
        pierwsza liczba
    b - int
        druga liczba
    i - int
        liczba służąca do reprezentacji, który krok rekurencji wykonujemy
    wynik - int
        zmieniający się dynamicznie (w zależności od kroku) efekt mnożenia (po ostatnim kroku jest wynikiem mnożenia a i b)

    Output:
    wynik - int
        wynik mnożenia wykonanego rekurencyjnie

    """
    if i == b:
        return wynik
    return mnozenie(a,b,i+1,wynik+a)

