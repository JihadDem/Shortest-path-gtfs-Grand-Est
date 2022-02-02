# Ce fichier lit stops.txt et insère dans 1.stops_center.csv les arrêts

from distance_to_center import distance_to_center
from math import radians
import csv

stops_src_file = open('../gtfs/stops.txt', 'r')
stops_src_reader = csv.DictReader(stops_src_file)

stops_center_file = open('./csv/1.stops_center.csv', 'w')
stops_center_writer = csv.writer(stops_center_file)

stops_center_writer.writerow( ('stop_id', 'stop_name') );
for row in stops_src_reader:
    stop_lat = radians(float(row['stop_lat']))
    stop_lon = radians(float(row['stop_lon']))
    dist = distance_to_center( stop_lat, stop_lon )
    if dist <= 5.63:
        curr_stop_id = row['stop_id']
        stops_center_writer.writerow( (curr_stop_id, row['stop_name']) );

stops_src_file.close();
stops_center_file.close();