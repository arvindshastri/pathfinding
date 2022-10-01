from abc import ABC, abstractmethod
from OutputHelpers import *

class Strategy(ABC):

    @abstractmethod
    def do_algorithm(self, graph, start_node, target_node):
        pass