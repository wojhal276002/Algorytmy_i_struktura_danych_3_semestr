class Empty(Exception):
    pass

class Queue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * Queue.DEFAULT_CAPACITY
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


    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        value= self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if self._size <= len(self._data)//2: #jeśli długość kolejki (size) jest mniejsza w danym momencie niż długość
            self.resize(len(self._data)//2) #kolejki (data), skracamy wielkość kolejki o połowę
        return value


    def enqueue(self, e):
        if self._size == len(self._data):
            self.resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):  # only
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
            if self._data[(self._front+i) % len(self._data)] != None:
                kolejka.append(self._data[(self._front+i)%len(self._data)])
            else:
                kolejka.append(" ")

        return f"{kolejka}"

if __name__=="__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(6)
    q.dequeue()
    q.enqueue(1)
    q.enqueue(1)
    q.dequeue()
    print(q)