class Empty(Exception):
    pass

class Stack:


    def __init__(self):
        self._data = []  # nowy


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

def Htmlowiec(plik):
    """
    Funkcja odpowiedzialna za sprawdzenie pliku html pod kątem brakujących znaczników zamykających

    Parametry:
    plik - str
        ścieżka do pliku z kodem html
    Output:
    informacja zwrotna, czy plik html jest poprawny pod kątem znaczników zamykających czy nie

    """
    stos = Stack()
    lista = ["area", "base", "br", "col", "command", "embed", "hr", "img", "input", "keygen", "link", "meta", "param", "source", "track", "wbr"]
    with open(f'{plik}', 'r') as file:
        html = file.read().replace('\n', '')
    for znaki in range(len(html)):
        if html[znaki] == "<":
            if html[znaki + 1] != "!" and html[znaki + 1] != "/":
                j = znaki + 1
                tag = ""
                while html[j] != ">" and html[j] != " ":
                    tag += html[j].lower()
                    j += 1
                if tag not in lista:
                    if tag[0:12] != "view-source:":
                        stos.push(tag)
            elif html[znaki + 1] == "/":
                j = znaki + 2
                tagi = ""
                while html[j] != ">" and html[j] != " ":
                    tagi += html[j].lower()
                    j += 1
                print(stos,tagi)
                if stos.is_empty():
                    return "Nieprawidłowy html, znaków zamykających więcej niż otwierających"
                if tagi == stos.top():
                    stos.pop()
                else:
                    return f"Nieprawidłowy html, znak otwierający, który przeszkodził: {stos.top()}"
    if stos.is_empty():
        return "Prawidłowy html"
    else:
        return f"Nieprawidłowy html, znak otwierający, który przeszkodził: {stos.top()}"

if __name__=="__main__":
    print(Htmlowiec('/Users/wojtek/Desktop/HTML_sample2.txt'))