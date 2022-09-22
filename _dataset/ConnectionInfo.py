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
    