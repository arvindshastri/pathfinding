from Metric import Metric


class AverageDegree(Metric):

    def numberOfNodes(self, graph):
        return len(graph.stationsDict)
    
    def numberOfDegreesPerNode(self, graph):

        degreeLengthDict = {}

        for node in graph.adj_list:

            mappedNode = node.get_id()

            if mappedNode in degreeLengthDict:
                degreeLengthDict[mappedNode] += len(graph.adj_list[node])
            else:
                degreeLengthDict[mappedNode] = len(graph.adj_list[node])

        return degreeLengthDict

    def compute_metric(self, graph):
        numDeg = sum( self.numberOfDegreesPerNode(graph).values() )
        return (numDeg / self.numberOfNodes(graph))
