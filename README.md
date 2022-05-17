# Graphes multimodaux et Shortest Path problems sur des instances réelles (jeux de données GTFS)



# Hello👋


## Création de données

• Importer les données GTFS en SQLite

• Construire l'horaire à partir de GTFS stop_times.txt

• Construire une liste de successeurs avec LMDB
## Algorithme

• L'algorithme de Dijkstra sur un modèle dépendant du temps
## Visualisation de graphiques

• Dessiner les nœuds du graphe dans l'interface graphique et imprimer les chemins optimaux
## Dépendances

Ce projet a été construit avec :


| Module | Version     | Description                |
| :-------- | :------- | :------------------------- |
| python | 3.9.7 |  |
| SQLite | 3.38.0 | Stockage des données de fichiers SQL pour les requêtes GTFS |
| LMDB | 1.1.1 | stockage de valeur-clé pour la liste des successeurs |
| MatPlotLib | 3.5.2 | Bibliothèque de traçage 2D |
| PyQt | 5.15.6 |  Adaptateur python Qt |





## Jeu de données GTFS

Vous pouvez télécharger les jeux de données GTFS sur https://navitia.io/datasets. J'ai utilisé et testé le jeu de données de transport sur la region Grand-Est (https://navitia.opendatasoft.com/explore/dataset/fr-ne/table/), mais il fonctionne avec la plupart des jeux de données GTFS (les valeurs par défaut pour la réduction des arrêts sont spécifiques à ce jeu de données).

Une fois téléchargé, extrayez le fichier .zip et sélectionnez l'option "create folder as workspace" dans l'exécution du logiciel.
