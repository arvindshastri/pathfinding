class Line:

    def __init__(self, line, name, colour, stripe):
        self.line = line
        self.name = name
        self.colour = colour
        self.stripe = stripe

    # getters
    def get_line(self):
        return self.line

    def get_name(self):
        return self.name

    def get_colour(self):
        return self.colour

    def get_stripe(self):
        return self.stripe

    # setters
    def set_line(self, line):
        self.line = line

    def set_name(self, name):
        self.name = name
