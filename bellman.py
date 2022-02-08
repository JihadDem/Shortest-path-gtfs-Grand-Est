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
            for dist, neighbour in graph[node]:
                if neighbour not in distance:
                    distance[neighbour] = float('inf');
                # Si la distance entre le nœud et le voisin est inférieure à la distance actuelle, store-la.
                if distance[neighbour] > distance[node] + dist:
                    distance[neighbour], predecessor[neighbour] = distance[node] + dist, node

     # Etape 3: Check les cycle négatifs de poids
    for node in graph:
        for dist, neighbour in graph[node]:
            assert distance[neighbour] <= distance[node] + dist, "Negative weight cycle."

    return distance,predecessor

# le prédécesseur qui est un dictionnaire sera le résultat trouvé dans bellman_ford
id2name = eval( open('../data_generation/output/id2name.json', 'r').read() );
def shortest_way(predecessor, source, origin):
    way = [id2name[origin][0].replace('\u00e9', 'é')]
    start = origin
    while True:
        if predecessor[start] == source:
            break;
        start = predecessor[start]
        way.append(id2name[start][0].replace('\u00e9', 'é'))
    way.append(id2name[source][0].replace('\u00e9', 'é'))
    return way;

graph = eval( open('../data_generation/output/graph_pred.json', 'r').read() );

starting_node = "StopPoint:OIF59587"; # Gare de Strasbourg
end_node = "StopPoint:OIF59659"; # Reims

distance, predecessor = bellman_ford(graph, starting_node)
# {'a': 0, 'c': 4, 'b': 1, 'e': 3, 'd': 3}, le plus court chemin vers 'a' depuis chaque noeud
print("Shortest distance from d to a:", distance[end_node])
# la distance la plus courte entre "b" et "a".
print("Shortest chemin from d to a:", shortest_way(predecessor, starting_node, end_node))
# le chemin le plus court de "d" à "a"