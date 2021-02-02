from typing import List

from src.geography.planet import Planet


class Route:
    name: str
    planets: List

    def __init__(self, name: str, planets: List):
        self.name = name
        self.planets = planets

    def add_planet(self, planet: Planet):
        self.planets.append(planet)
