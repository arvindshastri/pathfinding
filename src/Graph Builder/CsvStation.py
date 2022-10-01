import csv
from Station import *

def csvReaderStations(csv_stations_string):

    stations = {}

    with open(csv_stations_string, 'r') as csvStations:
        reader = csv.reader(csvStations)
        headers = next(reader)
        position = headers.index('id')
        for row in reader:
            index = row[position]
            stations[index] = Station(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
    
    return stations