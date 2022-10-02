from Metric import Metric


class DegreePerStation(Metric):

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
        
        degreesList = {}

        degreeLengthDict = self.numberOfDegreesPerNode(graph)
        
        for i in degreeLengthDict:
            deg = degreeLengthDict[i]
            if deg in degreesList:
                degreesList[deg] += 1
            else:
                degreesList[deg] = 1
        
        return degreesList
    