import os

lista = []
def find(path, filename):
    """
    Funkcja odpowiedzialna za znalezienie plików o podanej nazwie w podfolderach stworzonych wcześniej rekurencyjnie

    Parametry:
    path - str
        ścieżka, od której mamy rozpocząć szukanie plików
    filename - str
        nazwa pliku, którego szukamy
    Output:
    lista - list
        lista ścieżek do plików o nazwie, której szukaliśmy
        
    """
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            if item == filename:
                lista.append(os.path.join(path,item))
        elif os.path.isdir(os.path.join(path, item)):
            find(os.path.join(path, item), filename)
    return lista

if __name__=="__main__":
    print(find("/Users/wojtek/Desktop/folder_3", "wks.png"))
