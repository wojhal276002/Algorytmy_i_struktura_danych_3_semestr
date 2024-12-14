def palindrom(ciag):
    """
    Funkcja odpowiedzialna za sprawdzenie czy podany ciąg znaków/liczba jest palindromem

    Parametry:
    ciag - str/float
        ciąg znaków, który ma być sprawdzony pod kątem bycia palindromem
    Output:
    wiadomość, czy podany ciąg znaków jest lub nie palindromem

    """
    if type(ciag) == str:
        ciag = ciag.replace(" ","")
        ciag = list(ciag)
    if type(ciag) == float:
        ciag = list(str(ciag))
    if len(ciag) > 1:
        if ciag[0] == ciag[len(ciag)-1]:
            palindrom(ciag[1:len(ciag)-1])
        else:
            print("To nie jest palindrom")
    else:
        print("To jest palindrom")


palindrom(111.111)

