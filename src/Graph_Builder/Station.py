class Station():
    
    def __init__(self, id, latitude, longitude, name, display_name, zone, total_lines, rail):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.display_name = display_name 
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



