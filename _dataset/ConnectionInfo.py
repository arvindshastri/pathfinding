import csv

class ConnectionInfo:

    def __init__(self, line, time):
        self.line = line
        self.time = time

    def get_line(self):
        return self.line

    def get_time(self):
        return self.time
    