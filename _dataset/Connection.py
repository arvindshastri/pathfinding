import csv
import pprint
from ConnectionInfo import ConnectionInfo
from Station import csvReaderStations
from Line import csvReaderLines


class Connection:

    def __init__(self, station1, station2, information):
        self.station1 = station1
        self.station2 = station2
        self.information = information

    def get_station1(self):
        return self.station1

    def get_station2(self):
        return self.station2

    def get_information(self):
        return self.information


def csvReaderConnections(lines, stations):

    connections = []

    with open('london.connections.csv', 'r') as csvLines:
        reader = csv.reader(csvLines)
        next(reader)
        
        for row in reader:
            
            station1 = stations[row[0]]
            station2 = stations[row[1]]
            line = lines[row[2]]
            time = row[3]
            
            tempConnectionInfo = ConnectionInfo(line, time)
            tempConnection = Connection(station1, station2, tempConnectionInfo)
            connections.append(tempConnection)
    
    return connections

tempLines = csvReaderLines()
tempStations = csvReaderStations()
tempConnections = csvReaderConnections(tempLines, tempStations)
pprint.pprint(tempLines)
pprint.pprint(tempStations)
# pprint.pprint(tempConnections)
    