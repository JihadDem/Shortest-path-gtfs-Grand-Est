def shortest_path(arcIterator, start, end, departure_time = None):
    class DataStore:
        def __init__(self, default_value):
            self.default_value = default_value;
            self.dict = {};
        def get(self, stop_id):
            try:
                return self.dict[stop_id];
            except:
                return self.default_value;
        def set(self, stop_id, value):
            if (value != self.default_value):
                self.dict[stop_id] = value;

    # IValeurs d'initialisationnit values
    d = DataStore(float('inf')); # définit toutes les distances à +inf
    d.set(start, 0);
    p = DataStore(None); # met tous les prédécesseurs à None

    # calcule n
    n = len( arcIterator );

    # Exec Bellman-Ford
    for _ in range(n - 1):
        for u, v, h, w in arcIterator:
            if( d.get(v) > d.get(u) + w ):
                d.set(v, d.get(u) + w);
                p.set(v, u);

    # resultat formage
    result = [end];
    x = end;
    while x != start:
        x = p.get(x);
        result += [x];

    return result, d.get(end);