import os

def folder_tworzacz(path, folders):
    """
    Funkcja odpowiedzialna za rekurencyjne stworzenie konkretnej liczby podfolderów w sobie

    Parametry:
    path - str
        ścieżka, gdzie ma być najmniej zagłębiony folder
    folders - int
        liczba folderów
    Output:
    stworzenie owych folderów

    """
    sciezka = os.path.join(path, f"folder_{folders}")
    if folders == 1:
        os.mkdir(sciezka)
    else:
        os.mkdir(sciezka)
        folder_tworzacz(sciezka, folders-1)

folder_tworzacz("/Users/wojtek/Desktop/", 3)
