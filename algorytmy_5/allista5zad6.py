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

def szybkie_sortowanie(arr):
    #tworzenie stosu, na który bedzie dodawane graniczne wartosci przedziałów rozważanych
    stos = Stack()
    #inicjacja pierwszych takowych wartości
    start,stop = 0, len(arr)-1
    #na stos
    stos.push(start)
    stos.push(stop)
    #dopóki nie przejdziemy całości
    while not stos.is_empty():
        #wyciągamy wartości i oznaczamy pivota
        stop = stos.pop()
        start = stos.pop()
        piv = arr[stop]
        index = start
        #dla elementów z przedziału jeśli jest on mniejszy niż pivot zamieniamy go z elementem większym niż pivot na pozycji index
        for elem in range(start,stop):
            if arr[elem] <= piv:
                arr[elem], arr[index]=arr[index],arr[elem]
                index += 1
        #zamieniamy element większy od pivota z pivotem miejscami
        arr[index],arr[stop]=arr[stop],arr[index]
        #jeśli index-1 > początek przedziału to na stos dajemy przedział do index-1
        if index-1 > start:
            stos.push(start)
            stos.push(index-1)
        #jeśli index+1 < koniec przedziału to na stos dajemy przedział od index+1
        if index+1 < stop:
            stos.push(index+1)
            stos.push(stop)
    return arr

if __name__ == "__main__":
    print(szybkie_sortowanie([21,0,6,5,60,2,40,142,8,7,1,10,60]))