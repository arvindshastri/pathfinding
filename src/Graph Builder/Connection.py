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

def connectionBuilder(station1, station2, line, time):
    CIname1 = "Station{0}toStation{1}".format(str(station1.get_id()), str(station2.get_id()))
    tempConnectionInfo1 = ConnectionInfo(line, time)
    tempConnectionInfo1.set_name(CIname1)
    tempConnection1 = Connection(station1, station2, tempConnectionInfo1)
    
    return tempConnection1
