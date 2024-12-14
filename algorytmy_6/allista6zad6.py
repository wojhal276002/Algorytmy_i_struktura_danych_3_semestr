from allista6zad1_2_3_4_5 import Graph

g = Graph()
#stan pierwotny - kolejno liczba misjonarzy, kanibali i wskazanie False/True czy łódka jest przy brzegu startowym
start = (3,3,1)
g.add_vertex(start)
#stany przyjmowane przez łódkę w czasie podróży
stany = [(1,0,1), (2,0,1), (0,1,1), (0,2,1), (1,1,1)]
probable = [(3,3,1)]
new_probable = []
visited = [(3,3,1)]

#pętla w celu wyznaczenia drogi tak aby wszyscy przeszli na drugi brzeg
while True:
    #jeśli łódka na brzegu startowym
    if probable[0][2] == 1:
        for node in probable:
            for lodka in stany:
                #stan układu po przepłynięciu łódki
                druga_strona = (node[0]-lodka[0],node[1]-lodka[1],node[2]-lodka[2])
                #warunki które muszą zaistnieć by kanibale nie zeżarli misjonarzy biednych
                if (druga_strona[0] == druga_strona[1] or druga_strona[0] == 3 or druga_strona[0] == 0) and 3 >= druga_strona[0] >= 0 and 3 >= druga_strona[1]>=0:
                    #dodanie stanu do odwiedzonych, stworzenie połączeń
                    if druga_strona not in visited:
                        new_probable.append(druga_strona)
                        visited.append(druga_strona)
                    g.add_edge(node,druga_strona)
    #zamiana listy stanów na aktualne rozpatrywane
    probable = new_probable
    #przerwanie pętli jeśli dotarliśmy do celu
    if (0,0,0) in probable:
        break
    new_probable = []
    #jeśli łódka na brzegu docelowym
    if probable[0][2] == 0:
        for node in probable:
            for lodka in stany:
                # stan układu po przepłynięciu łódki
                powrot = (node[0]+lodka[0],node[1]+lodka[1],node[2]+lodka[2])
                # warunki które muszą zaistnieć by kanibale nie zeżarli misjonarzy biednych
                if (powrot[0] == powrot[1] or powrot[0] == 3 or powrot[0] == 0) and 3 >= powrot[0] >= 0 and 3 >= powrot[1] >= 0:
                    # dodanie stanu do odwiedzonych, stworzenie połączeń
                    if powrot not in visited:
                        new_probable.append(powrot)
                        visited.append(powrot)
                    g.add_edge(node, powrot)
    # zamiana listy stanów na aktualne rozpatrywane
    probable = new_probable
    new_probable = []

print(g.visualize())
