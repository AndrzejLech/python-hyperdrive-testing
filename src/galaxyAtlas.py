import random
from typing import List

from src.geography.planet import Planet


class GalaxyAtlas:
    planets: List = []

    def create_or_update_planet(self, name: str):
        for planet in self.planets:
            if planet.name == name:
                return planet
        self.planets.append(Planet(name, []))
        return Planet(name, [])

    def get_random_planet(self):
        return random.choice(self.planets)
