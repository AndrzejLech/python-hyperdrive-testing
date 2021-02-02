from typing import List


class Planet:
    name: str
    neighbours: List

    def __init__(self, name: str, neighbours: List):
        self.name = name
        self.neighbours = neighbours

    def add_neighbour(self, planet):
        self.neighbours.append(planet)
