class Empty(Exception):
    pass

class DoubleQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * DoubleQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def delete_first(self):
        """
        Funkcja odpowiedzialna za usunięcie 1. elementu kolejki

        Output:
        value - float
            wartość usunięta

        """
        if self.is_empty():
            raise Empty('Queue is empty')
        value = self._data[self._front]
        self._data[self._front] = None
        for el in range(self._size):
            self._data[el] = self._data[(el+1) % len(self._data)]
        self._size -= 1
        return value

    def delete_last(self):
        """
                Funkcja odpowiedzialna za usunięcie ostatniego elementu kolejki

                Output:
                value - float
                    wartość usunięta

                """
        if self.is_empty():
            raise Empty('Queue is empty')
        value = self._data[(self._front+self._size-1)%len(self._data)]
        self._data[(self._front+self._size-1)%len(self._data)] = None
        self._size -= 1
        return value

    def add_last(self, e):
        """
                Funkcja odpowiedzialna za dodanie do kolejki na jej końcu elementu

                Parametry:
                e - float
                    element
                Output:
                kolejka z dodanym elementem na końcu

                """
        if self._size == len(self._data):
            self.resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def add_first(self, e):
        """
                Funkcja odpowiedzialna za dodanie do kolejki na jej początku elementu

                Parametry:
                e - float
                    element
                Output:
                kolejka z dodanym elementem na początku

                """
        if self._size == len(self._data):
            self.resize(2 * len(self._data))
        self._size += 1
        for el in range(self._size,0,-1):
            self._data[el] = self._data[(el-1)%len(self._data)]
        self._data[self._front] = e

    def resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def __str__(self):
        """
                Funkcja odpowiedzialna za reprezentację kolejki w postaci stringa

                Output:
                Wyprintowana kolejka w postaci listy

                """
        kolejka = []
        for i in range(len(self._data)):
            if self._data[i] == None:
                kolejka.append(" ")
            else:
                kolejka.append(self._data[i])
        return f"{kolejka}"

if __name__=="__main__":
    kolejka = DoubleQueue()
    kolejka.add_last(1)
    kolejka.add_last(3)
    kolejka.add_first(10)
    kolejka.delete_last()
    kolejka.add_first(2)
    kolejka.delete_first()
    kolejka.add_first(10)
    kolejka.delete_first()
    print(kolejka)
