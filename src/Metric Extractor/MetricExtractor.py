import matplotlib.pyplot as plt    

def numberOfNodes(graph):
    return len(graph.stationsDict)

def numberOfConnections(graph):     
    return len(graph.connectionsList) / 2

def numberOfDegreesPerNode(graph):
    
    degreeLengthDict = {}

    for node in graph.adj_list:
        
        mappedNode = node.get_id()

        if mappedNode in degreeLengthDict: 
            degreeLengthDict[mappedNode] += len(graph.adj_list[node])
        else: 
            degreeLengthDict[mappedNode] = len(graph.adj_list[node])
        
        for i in graph.adj_list[node]:
            
            connectingStation = i[0].get_id()

            if connectingStation in degreeLengthDict: 
                degreeLengthDict[connectingStation] += 1
            else: 
                degreeLengthDict[connectingStation] = 1

    return degreeLengthDict


def numberOfDegreesPerStation(graph):
    
    degreesList = {}

    degreeLengthDict = numberOfDegreesPerNode(graph)
    
    for i in degreeLengthDict:
        deg = degreeLengthDict[i]
        if deg in degreesList:
            degreesList[deg] += 1
        else:
            degreesList[deg] = 1
    
    return degreesList
    

def averageDegree(graph):
    numDeg = sum(numberOfDegreesPerNode(graph).values())
    return (numDeg / numberOfNodes(graph))


def plotDegreeFrequency(graph):
    degreeLengthDict = numberOfDegreesPerStation(graph)

    degreeKeys = list(degreeLengthDict.keys())
    degreeValues = list(degreeLengthDict.values())

    plt.bar(degreeKeys, degreeValues)
  
    plt.xlabel('Degree of Nodes')
    plt.ylabel('Frequency')
    plt.title('Degree of Nodes vs Frequency')
    plt.show()
        
    return 
