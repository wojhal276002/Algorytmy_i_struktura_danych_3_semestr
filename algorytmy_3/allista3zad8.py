import math

class Empty(Exception):
    pass


class Stack:
    def __init__(self):
        self._data = []  # nowy pusty stos

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

    def __str__(self):
        return str(self._data)

def permutacja(lista):
    """
    Funkcja odpowiedzialna za wypisanie wszystkich permutacji liczb [1,2,...n] w liście

    Parametry:
    lista - list
        lista elementów do spermutowania
    Output:
    wszystkie - list
        lista wszystkich permutacji

    """
    stos = Stack()
    wszystkie = []
    for n in range(len(lista)):
        stos.push([lista[n]])
        pusta = []
        char = lista
        while True:
            c = stos.top()
            for i in char:
                f = c.copy()
                if not i in f:
                    f.append(i)
                    pusta.append(f)
            stos.pop()
            if stos.is_empty():
                if len(pusta[0]) != len(lista):
                    for k in pusta:
                        stos.push(k)
                    pusta.clear()
                else:
                    wszystkie.extend(pusta)
                    break
    return wszystkie

if __name__=="__main__":
    print(permutacja([1,2,3,4]))


