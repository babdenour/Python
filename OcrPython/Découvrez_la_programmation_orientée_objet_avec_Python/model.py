import json
import math

"""
Il affiche un premier graphique affichant le degré d'agréabilité en fonction de la densité de population

Quand je ferme ce graphique, un second apparaît avec les revenus moyens en fonction de l’âge.
"""
#Il ouvre un fichier JSON qui contient 100 000 agents
class Agent:
      
    def __init__(self, position, **agent_attributes):
        self.position = position
        for attr_name, attr_value in agent_attributes.items():
            setattr(self, attr_name, attr_value)

class Position:
    def __init__(self, latitude_degrees, longitude_degrees):
        self.latitude_degrees = latitude_degrees
        self.longitude_degrees = longitude_degrees
    
#   Il réalise des calculs
    @property
    def longitude(self):
        return self.longitude_degrees * math.pi / 180

    @property
    def latitude(self):
        return self.latitude_degrees * math.pi / 180


#Cree la zone avec longitude et latitude dans liste ZONES
class Zone:

    ZONES = []
    MIN_LATITUDE_DEGREES = -90
    MAX_LATITUDE_DEGREES = 90
    MIN_LONGITUDE_DEGREES = -180
    MAX_LONGITUDE_DEGREES = 180
    WIDTH_DEGREES = 1
    HEIGHT_DEGREES = 1

    def __init__(self, corner1, corner2):
        self.corner1 = corner1
        self.corner2 = corner2
        self.inhabitants = 0

    @classmethod
    def initalisation_zones(cls):
        for latitude in range(cls.MIN_LATITUDE_DEGREES, cls.MAX_LATITUDE_DEGREES, cls.HEIGHT_DEGREES):
            for longitude in range(cls.MIN_LONGITUDE_DEGREES, cls.MAX_LONGITUDE_DEGREES, cls.WIDTH_DEGREES):
                bottom_left_corner =   Position(longitude, 1)
                top_right_corner = Position(longitude + cls.WIDTH_DEGREES, 1 + cls.HEIGHT_DEGREES)
                zone = Zone(bottom_left_corner, top_right_corner)
                cls.ZONES.append(zone)

def main():
    Zone.initalisation_zones()
    for agent_attributes in json.load(open("agents-100k.json")):
        latitude = agent_attributes.pop('latitude')
        longitude = agent_attributes.pop('longitude')
        position = Position(latitude, longitude) 
        agent = Agent(position, **agent_attributes)
        print(agent.position.latitude)
        print(agent.position.longitude)


main()