import matplotlib.pyplot as plt
import numpy as np
import random

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
#algorytm jak w zadaniu 6
#tworzymy randomową listę elementów
arr = [random.randint(0,1000) for i in range(20)]
print(arr)
stos = Stack()
start,stop = 0, len(arr)-1
stos.push(start)
stos.push(stop)
#inicjacja początkowego wyglądu listy
plt.bar(list(range(len(arr))), arr)
plt.pause(0.1)
plt.clf()

while not stos.is_empty():
    stop = stos.pop()
    start = stos.pop()
    piv = arr[stop]
    index = start
    for elem in range(start,stop):
        if arr[elem] <= piv:
            bars0 = plt.bar(list(range(len(arr))), arr)
            #przedzial ktory rozwazamy-niebieski
            for i in range(start,stop):
                bars0[i].set_color('b')
            #pivot-różowy
            bars0[stop].set_color('#ff00ff')
            #dwa zamieniane elementy-czerwony
            bars0[elem].set_color('r')
            bars0[index].set_color('r')
            plt.pause(0.1)
            plt.clf()
            arr[elem], arr[index]=arr[index],arr[elem]
            index += 1
            bars1 = plt.bar(list(range(len(arr))), arr)
            # przedzial ktory rozwazamy-niebieski
            for i in range(start,stop):
                bars1[i].set_color('b')
            # pivot-różowy
            bars1[stop].set_color('#ff00ff')
            plt.pause(0.1)
            plt.clf()
    bars2 = plt.bar(list(range(len(arr))), arr)
    #pivot-różowy
    bars2[stop].set_color('#ff00ff')
    plt.pause(0.1)
    plt.clf()
    arr[index],arr[stop]=arr[stop],arr[index]
    if index-1 > start:
        stos.push(start)
        stos.push(index-1)
    if index+1 < stop:
        stos.push(index+1)
        stos.push(stop)
#wygląd listy w ostateczności
plt.bar(list(range(len(arr))),arr)
plt.pause(0.1)
plt.clf()
print(arr)
plt.show()