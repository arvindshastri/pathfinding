from Metric import Metric


class NodeNumber(Metric):

    def compute_metric(self, graph):
        return len(graph.stationsDict)
