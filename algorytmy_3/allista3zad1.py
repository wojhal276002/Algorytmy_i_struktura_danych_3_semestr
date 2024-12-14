import ctypes

class DynamicArray:
    def __init__(self):
        self._n = 0 #liczba elementów
        self._capacity = 1 #rozmiar tablicy
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self,k):
        if not 0<=k<self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()
    def insert(self, k, value):
        """
        Funkcja odpowiedzialna za dodanie elementu na pozycji k

        Parametry:
        k - int
            pozycja, na którą ma zostać dodany element
        value - float
            element mający zostać dodany
        Output:
        Obiekt klasy DynamicArray z dodanym na pozycji k elementem

        """
        if k > self._n:
            while k > self._capacity:
                self._resize(2 * self._capacity)
            for i in range(k-self._n):
                self.append(" ")
            self.append(value)
        else:
            if self._n + 1 == self._capacity:
                self._resize(2 * self._capacity)
            self.append(" ")
            for i in range(self._n, k, -1):
                self._A[i] = self._A[i - 1]
            self._A[k] = value


    def remove(self,value):
        """
                Funkcja odpowiedzialna za usunięcie danego elementu (wszystkich takich)

                Parametry:
                value - float
                    element mający zostać usunięty
                Output:
                Obiekt klasy DynamicArray bez elementów usuniętych

                """
        for k in range(self._n):
            if self._A[k] == value:
                self._A[k] = " "

    def expand(self, seq):
        """
                Funkcja odpowiedzialna za rozszerzenie tablicy o podane elementy

                Parametry:
                seq - list
                    lista elementów, o które ma zostać rozszerzona tablica
                Output:
                Obiekt klasy DynamicArray rozszerzone o elementy z listy

                """
        while self._n + len(seq) > self._capacity:
            self._resize(2*self._capacity)
        for i in range(len(seq)):
            self.append(seq[i])

    def __str__(self):
        """
                Funkcja odpowiedzialna za reprezentację tablicy w postaci stringa

                Output:
                Wyprintowana tablica typu |element1|element2|itd.

                """
        string = "|"
        for i in range(self._n):
            string += (str(self._A[i])+"|")
        for i in range(self._capacity-self._n):
            string += " |"
        return string

if __name__=="__main__":
    tablica = DynamicArray()
    tablica.append(11)
    tablica.append(1)
    tablica.append(11)
    tablica.append(1)
    tablica.insert(0,0)
    print(tablica)