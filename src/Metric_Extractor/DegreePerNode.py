from Metric import Metric


class DegreePerNode(Metric):

    def compute_metric(self, graph):

        degreeLengthDict = {}

        for node in graph.adj_list:

            mappedNode = node.get_id()

            if mappedNode in degreeLengthDict:
                degreeLengthDict[mappedNode] += len(graph.adj_list[node])
            else:
                degreeLengthDict[mappedNode] = len(graph.adj_list[node])

        return degreeLengthDict
