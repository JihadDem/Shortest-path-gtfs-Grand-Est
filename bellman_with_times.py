from structures.arc_iterator import GraphArcIterator;
from algorithms.bellman_with_hours import shortest_path;

arcIterator = GraphArcIterator( './data_generation/output/sub' );

print( shortest_path(arcIterator, 'z', 'y') );