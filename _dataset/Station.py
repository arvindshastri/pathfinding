import csv

class Station():
    
    def __init__(self, name, id, latitude, longitude, display_name, zone, total_lines, rail):
        self.name = name
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.display_name = display_name
        self.zone = zone
        self.total_lines = total_lines
        self.rail = rail


def csvReaderStations():

    stations = {}

    with open('london.stations.csv', 'r') as csvStations:
        reader = csv.reader(csvStations)
        headers = next(reader)
        position = headers.index('id')
        for row in reader:
            index = row[position]
            stations[index] = Station(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
    
    return stations