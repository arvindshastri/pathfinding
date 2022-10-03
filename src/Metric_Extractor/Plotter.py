import matplotlib.pyplot as plt
from Metric import Metric


class Plotter(Metric):

    def numberOfDegreesPerNode(self, graph):

        degreeLengthDict = {}

        for node in graph.adj_list:

            mappedNode = node.get_id()

            if mappedNode in degreeLengthDict:
                degreeLengthDict[mappedNode] += len(graph.adj_list[node])
            else:
                degreeLengthDict[mappedNode] = len(graph.adj_list[node])

        return degreeLengthDict

    def numberOfStationsPerNode(self, graph):

        degreesList = {}

        degreeLengthDict = self.numberOfDegreesPerNode(graph)

        for i in degreeLengthDict:
            deg = degreeLengthDict[i]
            if deg in degreesList:
                degreesList[deg] += 1
            else:
                degreesList[deg] = 1

        return degreesList

    def compute_metric(self, graph):
        degreeLengthDict = self.numberOfStationsPerNode(graph)
        degreeKeys = list(degreeLengthDict.keys())
        degreeValues = list(degreeLengthDict.values())

        plt.bar(degreeKeys, degreeValues)
        plt.xlabel('Degree of Nodes')
        plt.ylabel('Frequency')
        plt.title('Degree of Nodes vs Frequency')
        plt.show()
        print("Degree of Nodes vs Frequency Values: ", degreeLengthDict)

        return
