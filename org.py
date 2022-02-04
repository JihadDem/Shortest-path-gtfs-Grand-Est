#La bibliothèque standard "heapq" fournit les fonctions de manipulation d'un
# tas.Juste ce qu'il nous faut pour implémenter la file des sommets à traiter.

from heapq import *

#Implémentation de l'algorithme de Dijkstra en Python.
#
# Les arguments sont:
# s : le sommet source
# t : le sommet but
# voisins : fonction qui pour un sommet renvoie une liste de couples
# (poids, sommet) pour chaque arête sortante
#Les sommets doivent être des objets "hachables" (nombres, chaînes de
#caractères, n-uplets...).

def dijkstra (s, t, voisins):
    M = set()
    d = {s: 0}
    p = {}
    suivants = [(0, s)] #tas de couples (d[x],x)
    n_step = 0;

    while suivants != []:

        dx, x = heappop(suivants)
        if x in M:
            continue
        n_step = n_step + 1;
        M.add(x)

        for w, y in voisins(x):
            if y in M:
                continue
            dy = dx + w
            if y not in d or d[y] > dy:
                d[y] = dy
                heappush(suivants, (dy, y))
                p[y] = x

    path = [t]
    x = t
    while x != s:
        x = p[x]
        path.insert(0, x)

    print(n_step);
    return d[t], path


#Exemple d'utilisation avec un graphe représenté par une liste adjacente.

graph = {
    "A": [ (27, "D"), (2, "G") ],
    "B": [ (1, "A") ],
    "C": [ (1, "B"), (2, "F"), (3, "G") ],
    "D": [ (4, "G"), (7, "H") ],
    "E": [ (5, "A"), (3, "B"), (2, "C") ],
    "F": [ (8, "H"), (1, "D") ],
    "G": [ (4, "F") ],
    "H": []
}

starting_node = "StopPoint:OIF59421"; # Gare de strasbourg
end_node = "StopPoint:OIF59657"; # Cathédrale Reims

graph = eval ( open('../gui/tmp/14.successors_list.csv', 'r').read() );

def voisins (s):
    try:
        r = graph[s]
    except:
        r = []
    return r;

print(dijkstra(starting_node,end_node,voisins));