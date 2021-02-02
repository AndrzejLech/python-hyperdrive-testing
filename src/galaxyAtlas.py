import random
from typing import List

from src.geography.planet import Planet


class GalaxyAtlas:
    planets: List = []

    def create_or_update_planet(self, new_planet: Planet):
        for planet in self.planets:
            if planet.name == new_planet.name:
                return planet
        self.planets.append(new_planet)
        return new_planet

    def get_random_planet(self):
        return random.choice(self.planets)
