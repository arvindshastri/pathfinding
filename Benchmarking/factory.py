# Shortest path algorithm collections

import algorithms as algo
from interface import ShortAlgorithm


class SortingFactory():

    @staticmethod
    def build(name: str) -> ShortAlgorithm:
        selected = None
        match name:
            case 'a*':
                selected = algo.A_star()
            case 'dijkstra':
                selected = algo.Dijkstra()
            case _:
                raise ValueError(name)
        return selected
