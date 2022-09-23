import csv

class ConnectionInfo:

    name = ""

    def __init__(self, line, time):
        self.line = line
        self.time = time

    def get_line(self):
        return self.line

    def get_time(self):
        return self.time

    def get_name(self):
        return self.name
    
    def set_name(self, string):
        self.name = string
    

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


def csvReaderConnections(londonConnections, lines, stations):

    connections = []

    with open(londonConnections) as csvLines:
        reader = csv.reader(csvLines)
        next(reader)
        
        for row in reader:
            
            station1 = stations[row[0]]
            station2 = stations[row[1]]
            line = lines[row[2]]
            time = row[3]

            CIname = "Station{0}toStation{1}".format(str(station1.get_id()), str(station2.get_id()))
            tempConnectionInfo = ConnectionInfo(line, time)
            tempConnectionInfo.set_name(CIname)
            tempConnection = Connection(station1, station2, tempConnectionInfo)
            connections.append(tempConnection)
    
    return connections
