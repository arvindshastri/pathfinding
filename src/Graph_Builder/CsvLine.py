import csv
from Line import *

def csvReaderLines(csv_lines_string):

    lines = {}

    with open(csv_lines_string, 'r') as csvLines:
        reader = csv.reader(csvLines)
        headers = next(reader)
        position = headers.index('line')
        for row in reader:
            index = row[position]
            lines[index] = Line(row[0], row[1], row[2], row[3])
    
    return lines