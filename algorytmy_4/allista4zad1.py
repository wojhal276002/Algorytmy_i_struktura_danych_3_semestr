import time
import matplotlib.pyplot as plt

class Empty(Exception):
    pass


class LinkedStack:
    #--- Node class ---
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
    #--- Stack methods ---
    def __init__(self):  # empty
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty!')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

def czasomierzator(odstep, elem, num, push=False, pop=False, top=False):
    """
        Funkcja odpowiedzialna za zmierzenie czasów metody jednej z metod stosu przy pomocy listy jednokierunkowej

        Parametry:
        odstep - int
            co ile ma być indeks mierzonego czasu
        elem - int
            liczba elementów w liście głównej
        num - int
            liczba powtórzeń wykonania metody dla każdego indeksu
        push,pop,top - bool
            sprecyzowanie której metody chcemy zmierzyć czas

        Output:
        lista_czasow - list
            lista z czasami, w jakich wykonuje się program dla różnych długości stosu

        """
    lista_czasow = []
    c = LinkedStack()
    for i in range(elem):
        c.push(1)
    for i in range(0,odstep*10,odstep):
        czas = 0
        for j in range(odstep):
            c.push(1)
        if push == True:
            for n in range(num):
                start = time.time()
                c.push(1)
                end = time.time()
                c.pop()
                print(c.__len__())
                czas += end - start
            lista_czasow.append(czas / num)
        if pop == True:
            for n in range(num):
                start = time.time()
                c.pop()
                end = time.time()
                c.push(1)
                czas += end - start
            lista_czasow.append(czas / num)
        if top == True:
            for n in range(num):
                start = time.time()
                c.top()
                end = time.time()
                czas += end - start
            lista_czasow.append(czas / num)
    return lista_czasow

# trzy różne metody
czas1 = czasomierzator(10000, 1000, 150, pop=True)
czas2 = czasomierzator(10000, 1000, 150, push=True)
czas3 = czasomierzator(10000, 1000, 150, top=True)

skala = range(0, 100000, 10000)

plt.plot(skala, czas1, "bo", label="pop")
plt.plot(skala, czas2, "ro", label="push")
plt.plot(skala, czas3, "yo", label="top")
ax = plt.gca()
ax.set_ylim(-0.0001, 0.0001)
print(czas1,"\n",czas2,"\n",czas3)
plt.title("Porównanie długości wykonywania metody extend i wielokrotnego append od czasu ", size=10)
plt.xlabel("Długość łączna listy")
plt.ylabel("Czas")
plt.legend()
plt.show()