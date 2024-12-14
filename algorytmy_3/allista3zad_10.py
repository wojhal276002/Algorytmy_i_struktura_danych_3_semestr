class Empty(Exception):
    pass

class Stack:


    def __init__(self):
        self._data = []


    def __len__(self):
        return len(self._data)


    def is_empty(self):
        return len(self._data)==0

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
        return f"{self._data}"

class Queue_by_Stacks:
    def __init__(self):
        """

        Przedstawienie kolejki za pomocą 2 stosów

        """
        self.stack1 = Stack()
        self.stack2 = Stack()

    def __len__(self):
        """

        Długość kolejki jako długość stosu1

        """
        return len(self.stack1)

    def is_empty(self):
        """

        Sprawdzenie czy kolejka jest pusta jeśli oba stosy są puste

        """
        return self.stack1.is_empty() and self.stack2.is_empty()

    def first(self):
        """

        Pokazanie pierwszego elementu w kolejce przez pracę 2 stosów

        """
        if self.is_empty():
            raise Empty('Queue is empty')
        while len(self.stack1) > 0:
            self.stack2.push(self.stack1.pop())
        first = self.stack2.top()
        while len(self.stack2) > 0:
            self.stack1.push(self.stack2.pop())
        return first

    def dequeue(self):
        """

        Wyrzucenie pierwszego elementu z kolejki za pomocą pracy 2 stosów

        """
        if self.is_empty():
            raise Empty('Queue is empty')
        while len(self.stack1) > 0:
            self.stack2.push(self.stack1.pop())
        last = self.stack2.pop()
        while len(self.stack2) > 0:
            self.stack1.push(self.stack2.pop())
        return last

    def enqueue(self,e):
        """

        Dodanie elementu e do kolejki (stosu1)

        """
        return self.stack1.push(e)

    def __str__(self):
        """

        Przedstawienie wizualne kolejki (stosu1)

        """
        return str(self.stack1)

if __name__=="__main__":
    a = Queue_by_Stacks()
    a.enqueue(2)
    a.enqueue(3)
    a.dequeue()
    a.enqueue(5)
    a.dequeue()
    print(a)
