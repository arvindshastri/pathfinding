from __future__ import annotations

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

import sys
from Dijkstra3 import Dijkstra
from A_Star3 import A_Star

sys.path.insert(1, '../../src/Graph_Builder') #running
#sys.path.insert(0, './src/Graph Builder') #debugging

from CsvLine import csvReaderLines
from CsvStation import csvReaderStations
from CsvConnection import csvReaderConnections
from GraphBuilder import GraphBuilder

londonLines = "./../../_dataset/london.lines.csv"
londonStations = "./../../_dataset/london.stations.csv"
londonConnections = "./../../_dataset/london.connections.csv"

# londonLines = "_dataset/london.lines.csv"
# londonStations = "_dataset/london.stations.csv"
# londonConnections = "_dataset/london.connections.csv"

tempStations = csvReaderStations(londonStations)
tempLines = csvReaderLines(londonLines)
tempConnections = csvReaderConnections(londonConnections, tempLines, tempStations)

graph = GraphBuilder(tempStations, tempLines, tempConnections)
graph.load_graph()

metric = MetricExtractor(graph)
metric._strategy = Dijkstra()
metric.algorithm('11', '200')
metric.print_output()
metric._strategy = A_Star()
metric.algorithm('11', '200')
metric.print_output()