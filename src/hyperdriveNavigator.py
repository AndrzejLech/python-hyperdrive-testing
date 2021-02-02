from src.galaxyAtlas import GalaxyAtlas
from src.geography.planet import Planet


class HyperdriveNavigator:
    atlas: GalaxyAtlas
    current_planet: Planet

    def __init__(self, atlas: GalaxyAtlas):
        self.atlas = atlas

    def get_current_planet(self):
        return self.current_planet

    def jump_to(self, planet: Planet):
        self.current_planet = planet

    def get_random_planet(self):
        self.current_planet = self.atlas.get_random_planet()
        return self.current_planet
