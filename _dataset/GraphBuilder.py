import csv
from tkinter.font import names


class Station:
    def __init__(self, name, id, latitude, longitude, display_name, zone, total_lines, rail):
        self.name = name
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.display_name = display_name
        self.zone = zone
        self.total_lines = total_lines
        self.rail = rail


class Lines:
    def __init__(self, line, name, colour, stripe):
        self.line = line
        self.name = name
        self.colour = colour
        self.stripe = stripe


my_list = []

with open('london.stations.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    for line in reader:
        my_list.append(Station(line[0]))
        print(my_list)
        


