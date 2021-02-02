import json
from types import SimpleNamespace
from typing import List

import yaml as yml

from src.galaxyAtlas import GalaxyAtlas
from src.geography.planet import Planet


class GalaxyAtlasBuilder:

    def build_from_routes_array(self, routes):
        atlas = GalaxyAtlas()
        self.build_planets(atlas, routes)
        return atlas

    def build_from_json(self, file_path: str):
        atlas = GalaxyAtlas()
        with open(file_path) as file:
            routes = json.load(file)
            self.build_planets(atlas, routes)
        return atlas

    def build_from_yml(self, file_path: str):
        atlas = GalaxyAtlas()
        with open(file_path) as file:
            routes = yml.load(file, Loader=yml.FullLoader)
        self.build_planets(atlas, routes.items())
        return atlas

    @staticmethod
    def build_planets(atlas: GalaxyAtlas, routes: List):
        for _, planets in routes:
            previous = None
            for name in planets:
                planet = Planet(name, [])
                planet = atlas.create_or_update_planet(planet)
                if previous is not None:
                    previous.add_neighbour(planet)
                    planet.add_neighbour(previous)
                previous = planet
