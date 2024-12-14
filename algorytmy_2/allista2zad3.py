def max_min(list, idx=1, max_i=0, min_i=0):
    """
    Funkcja odpowedzialna za zwrócenie największego i najmniejszego elementu sekwencji

    Parametry:
    list - list
        sekwencja
    idx - int
        index listy, od którego w zaczyna się dany krok rekurencji
    max_i - int
        index największego elementu w danym kroku
    min_i - int
        index najmniejszego elementu w danym kroku
    Output:
    odpowiedź na to, który element jest najmniejszy i największy w danej sekwencji

    """
    maks = list[max_i]
    mini = list[min_i]
    if idx == len(list):
        return f"(max,min)={maks, mini}"
    if list[idx] > maks:
        max_i = idx
    elif list[idx] < mini:
        min_i = idx
    return max_min(list, idx+1, max_i, min_i)

list = [71, 34, 54, 12, 32,8, 19,60,99]
print(max_min(list))