#Le graphique est un dictionnaire contenant une liste de prédécesseurs de chaque nœud.
# graph = {'stop_id1':[[precessor1, distance1],[precessor2, distance2], ...],
#           'stop_id2':[[precessor1, distance1],[precessor2, distance2], ...],
#           ...

def bellman_ford(graph, source):
    # Etape 1: Préparer la distance et le prédécesseur pour chaque nœud
    distance, predecessor = dict(), dict()
    for node in graph:
        distance[node], predecessor[node] = float('inf'), None
    distance[source] = 0

    # Étape 2 : Détendre les bords
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbour, dist in graph[node]:
                # Si la distance entre le nœud et le voisin est inférieure à la distance actuelle, store-la.
                if distance[neighbour] > distance[node] + dist:
                    distance[neighbour], predecessor[neighbour] = distance[node] + dist, node

     # Etape 3: Check les cycle négatifs de poids
    for node in graph:
        for neighbour, dist in graph[node]:
            assert distance[neighbour] <= distance[node] + dist, "Negative weight cycle."

    return distance,predecessor

# le prédécesseur qui est un dictionnaire sera le résultat trouvé dans bellman_ford
def shortest_way(predecessor, source, origin):
    way = [origin]
    start = origin
    while predecessor[start] is not source:
        start = predecessor[start]
        way.append(start)
    way.append(source)
    return way


# teste examples
graph = {
    'a':[['b', 1], ['c', 4]],
    'b':[['c', 3], ['d', 2], ['e', 2]],
    'c':[],
    'd':[['b', 1], ['c', 5]],
    'e':[['d', 3]]
}
distance, predecessor = bellman_ford(graph, source='a')
print(distance)
# {'a': 0, 'c': 4, 'b': 1, 'e': 3, 'd': 3}, le plus court chemin vers 'a' depuis chaque noeud
print("Shortest distance from d to a:", distance['d'])
# la distance la plus courte entre "b" et "a".
print("Shortest chemin from d to a:", shortest_way(predecessor, 'a', 'd'))
# le chemin le plus court de "d" à "a"