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
        if self._size <= len(self._data)//2:
            self.resize(len(self._data)//2)
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
        kolejka = []
        for i in range(len(self._data)):
            if self._data[(self._front+i) % len(self._data)] != None:
                kolejka.append(self._data[(self._front+i)%len(self._data)])
            else:
                kolejka.append(" ")

        return f"{kolejka}"

class Stack_by_Queue:
    def __init__(self):
        """
        Przedstawienie stosu jako obiektu kolejki

        """
        self.queue = Queue()

    def __len__(self):
        """
        Długość stosu

        """
        return len(self.queue)

    def is_empty(self):
        """
        Sprawdzenie czy stos jest pusty przy pomocy kolejki

        """
        return self.queue.is_empty()

    def push(self,e):
        """
        Dodanie elementu e na czubek stosu

        """
        self.queue.enqueue(e)

    def top(self):
        """
        Wychwycenie elementu na czubku stosu

        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.queue._data[(self.queue._front+self.queue._size-1)%len(self.queue)]

    def pop(self):
        """

        Wyrzucenie ze stosu elementu na jego czubku za pomocą kolejki

        """
        if self.is_empty():
            raise Empty('Stack is empty')
        for e in range(len(self.queue)-1):
            dequeued = self.queue.dequeue()
            self.queue.enqueue(dequeued)
        return self.queue.dequeue()

    def __str__(self):
        """

        Przedstawienie wizualne stosu

        """
        return str(self.queue)

if __name__=="__main__":
    s = Stack_by_Queue()
    s.push(4)
    s.push(9)
    s.push(2)
    s.push(4)
    s.push(9)
    s.push(2)
    s.pop()
    print(s)
#push O(n)
#pop O(1)
#top O(1)
#czemu ?