from Metric import Metric


class ConnectionNumber(Metric):

    def compute_metric(self, graph):
        count = 0

        for i in graph.connectionsList:
            count += 1

        return int(count/2)
