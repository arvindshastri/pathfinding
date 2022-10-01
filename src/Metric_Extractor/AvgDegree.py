import DegPerNode
import NodeNumber

def averageDegree(graph):
    numDeg = sum(numberOfDegreesPerNode(graph).values())
    return (numDeg / numberOfNodes(graph))