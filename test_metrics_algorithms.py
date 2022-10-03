import pytest  # noqa: F401
import sys

sys.path.append('.\src\Graph_Builder')  # noqa: W605
sys.path.append('.\src\Metric_Extractor')  # noqa: W605
sys.path.append('.\_dataset')  # noqa: W605

from CsvLine import csvReaderLines   # noqa: E402
from CsvStation import csvReaderStations   # noqa: E402
from CsvConnection import csvReaderConnections   # noqa: E402
from GraphBuilder import GraphBuilder   # noqa: E402
from MetricExtractor import MetricExtractor   # noqa: E402
from Dijkstra import Dijkstra   # noqa: E402
from A_Star import A_Star   # noqa: E402
from ConnectionNumber import ConnectionNumber   # noqa: E402
from AverageDegree import AverageDegree   # noqa: E402
from DegreePerStation import DegreePerStation   # noqa: E402
from NodeNumber import NodeNumber   # noqa: E402

londonLines = "_dataset/london.lines.csv"
londonStations = "_dataset/london.stations.csv"
londonConnections = "_dataset/london.connections.csv"

tempStations = csvReaderStations(londonStations)
tempLines = csvReaderLines(londonLines)
tempConnections = csvReaderConnections(
    londonConnections, tempLines, tempStations)

graph = GraphBuilder(tempStations, tempLines, tempConnections)
graph.load_graph()

analyzer = MetricExtractor(graph)

# functions defining metric computation


def connectionNumber():
    result = analyzer.compute_metric(ConnectionNumber())
    return result


def averageDegree():
    result = analyzer.compute_metric(AverageDegree())
    return result


def degreePerStation():
    result = analyzer.compute_metric(DegreePerStation())
    return result


def nodeNumber():
    result = analyzer.compute_metric(NodeNumber())
    return result


# pytests for metric computation


def test_connectionNumber():
    assert connectionNumber() == 406


def test_averageDegree():
    assert averageDegree() == 2.6887417218543046


def test_degreePerStation():
    assert degreePerStation() == {
        10: 1, 2: 191, 4: 43, 8: 4, 3: 15, 7: 2, 1: 24, 6: 16, 5: 5, 12: 1}


def test_nodeNumber():
    assert nodeNumber() == 302


# functioning defining Dijkstra output


analyzer._strategy = Dijkstra()  # set strategy to Dijkstra


def sameNodeDijkstra(start, end):  # same node twice
    result = analyzer.algorithm(start, end)
    return result


def neighbourNodeDijkstra(start, end):  # neighbouring node
    result = analyzer.algorithm(start, end)
    return result


# return True if start to end is the same as end to start

def reverseDijkstra(start, end):
    result = analyzer.algorithm(start, end)
    result2 = analyzer.algorithm(end, start)
    result3 = result2.reverse()  # noqa: F841
    return (result == result2)

# pytests for Dijkstra


def test_sameNodeDijkstra():
    assert sameNodeDijkstra('11', '11') is None


def test_neighbourNodeDijkstra():
    assert neighbourNodeDijkstra('11', '163') == ['11', '163']


def test_reverseDijkstra():
    assert reverseDijkstra('11', '200') is True


# functioning defining A* output

analyzer._strategy = A_Star()  # set strategy to A*


def sameNodeA_Star(start, end):  # same node twice
    result = analyzer.algorithm(start, end)
    return result


def neighbourNodeA_Star(start, end):  # neighbouring node
    result = analyzer.algorithm(start, end)
    return result

# return True if start to end is the same as end to start


def reverseA_Star(start, end):
    result = analyzer.algorithm(start, end)
    result2 = analyzer.algorithm(end, start)
    result3 = result2.reverse()  # noqa: F841
    return (result == result2)

# pytests for A*


def test_sameNodeA_Star():
    assert sameNodeA_Star('11', '11') is None


def test_neighbourNodeA_Star():
    assert neighbourNodeA_Star('11', '163') == ['11', '163']


def test_reverseA_Star():
    assert reverseA_Star('11', '200') is True
