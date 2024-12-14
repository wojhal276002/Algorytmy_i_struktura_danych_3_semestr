from allista6zad1_2_3_4_5 import Graph

g = Graph()
g.add_vertex((0,0))
#lista nodów które rozważamy
nody = []
#lista nodów które rozpatrzyliśmy
visited = []
nody.append((0,0))
visited.append((0,0))

def L_to_S(stan):
    pour_large = 3 - stan[1]
    if stan[0] - pour_large > 0:
        nowy = (stan[0] - pour_large, 3)
    else:
        nowy = (0, stan[1] + stan[0])
    return nowy

def S_to_L(stan):
    pour_small = 4 - stan[0]
    if stan[1] - pour_small >= 0:
        nowy = (4, stan[1] - pour_small)
    else:
        nowy = (stan[0] + stan[1], 0)
    return nowy

def waste_large(stan):
    return (0, stan[1])

def waste_small(stan):
    return (stan[0], 0)

def fill_large(stan):
    return (4, stan[1])

def fill_small(stan):
    return (stan[0], 3)

def if_in_list(node,lista,graph,node_0):
    if node not in visited:
        lista.append(node)
        visited.append(node)
    if node_0 != node and (str(node_0),str(node)) not in graph.get_edges():
        graph.add_edge(node_0, node)

#pętla po grafie, wykonanie każdej metody dla każdego noda który się pojawia w liście node
while nody != []:
    punkt = nody[0]
    a = waste_large(punkt)
    if_in_list(a,nody,g,punkt)
    b = waste_small(punkt)
    if_in_list(b, nody,g,punkt)
    c = fill_large(punkt)
    if_in_list(c, nody,g,punkt)
    d = fill_small(punkt)
    if_in_list(d, nody,g,punkt)
    e = L_to_S(punkt)
    if_in_list(e, nody,g,punkt)
    f = S_to_L(punkt)
    if_in_list(f,nody,g,punkt)
    nody = nody[1::]

print(g.visualize())






