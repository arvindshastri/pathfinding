import pyperf
import random
import sys
sys.path.append('.\src\Graph_Builder')
sys.path.append('.\src\Metric_Extractor')
sys.path.append('.\_dataset')
from CsvLine import csvReaderLines
from CsvStation import csvReaderStations
from CsvConnection import csvReaderConnections
from GraphBuilder import GraphBuilder
from A_Star3 import A_Star

def main():
    runner = pyperf.Runner()
    graph = graph_generation()
    randomNodes=random_nodes(graph)
    runner.bench_func('A_Star3', A_Star.do_algorithm, (graph,randomNodes[0],randomNodes[1]) )

def random_nodes(graph):
    stations = list(graph.get_stationsDict().values()) #syntax
    upper_bound = len(stations) - 1
    i=random.randint(0,upper_bound)
    j=random.randint(0,upper_bound)
    return [stations[i],stations[j]]

def graph_generation():
    londonLines = "_dataset/london.lines.csv"
    londonStations = "_dataset/london.stations.csv"
    londonConnections = "_dataset/london.connections.csv"

    tempStations = csvReaderStations(londonStations)
    tempLines = csvReaderLines(londonLines)
    tempConnections = csvReaderConnections(londonConnections, tempLines, tempStations)

    graph = GraphBuilder(tempStations, tempLines, tempConnections)
    graph.load_graph()
    return graph

main()
