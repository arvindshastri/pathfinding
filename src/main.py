import Line, Station, Connection, ConnectionInfo, GraphBuilder

from Line import csvReaderLines
from Station import csvReaderStations
from Connection import csvReaderConnections
from GraphBuilder import GraphBuilder
# from MetricExtractor import *

londonLines = r"D:\MacYear3\3XB3\L1Graph\l1-graph-lab\_dataset\london.lines.csv"
londonStations = r"D:\MacYear3\3XB3\L1Graph\l1-graph-lab\_dataset\london.stations.csv"
londonConnections = r"D:\MacYear3\3XB3\L1Graph\l1-graph-lab\_dataset\london.connections.csv"

tempStations = csvReaderStations(londonStations)
tempLines = csvReaderLines(londonLines)
tempConnections = csvReaderConnections(londonConnections, tempLines, tempStations)

graph = GraphBuilder(tempStations, tempLines, tempConnections)
graph.load_graph()
graph.print_graph()

# print(numberNodes(graph))
# print(numberConnections(graph))
# print(numberAvgDegree(graph))
# print(numberDegreesperNode(graph))
# print(plotNumberDegrees(graph))


