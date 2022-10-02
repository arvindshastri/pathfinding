from DegPerNode import numberOfDegreesPerNode
from NodeNumber import numberOfNodes


def averageDegree(graph):
    numDeg = sum(numberOfDegreesPerNode(graph).values())
    return (numDeg / numberOfNodes(graph))
