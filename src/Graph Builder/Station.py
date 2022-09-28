import csv

class Station():
    
    def __init__(self, id, latitude, longitude, name, display_name, zone, total_lines, rail):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.display_name = display_name #bad
        self.name = name
        self.zone = zone
        self.total_lines = total_lines
        self.rail = rail
    
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
    def get_latitude(self):
        return self.latitude
    
    def get_longitude(self):
        return self.longitude



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