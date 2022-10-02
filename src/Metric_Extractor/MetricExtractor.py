import Strategy
from OutputHelpers import *

class MetricExtractor():

    start_node = None
    target_node = None
    pathList = []
    infoList = []
    _strategy = None

    def __init__(self, graph) -> None:
        self.graph = graph
    
    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def setStrategy(self, strategy) -> None:
        self._strategy = strategy
    
    def algorithm(self, start_node, target_node) -> None:
        self.start_node = start_node
        self.target_node = target_node
        result = self._strategy.do_algorithm(self.graph, start_node, target_node)
        self.pathList = result
        
        return result
    
    def print_output(self):
        result = output_helper(self.graph, self.pathList)
        self.infoList = result
        prettyOutput(result)