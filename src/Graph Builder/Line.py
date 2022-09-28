import csv

class Line:

    def __init__(self, line, name, colour, stripe):
        self.line = line
        self.name = name
        self.colour = colour
        self.stripe = stripe
    
    def get_line(self):
        return self.line
    
    def get_name(self):
        return self.name
    
    def get_colour(self):
        return self.colour
    
    def get_stripe(self):
        return self.stripe

    def set_line(self):
        self.line = "TEST"
    
    def set_name(self):
        self.name = "TEST"



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



    

    
