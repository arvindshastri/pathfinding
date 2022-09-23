import matplotlib.pyplot as plt

def numberNodes(graph):
    count = 0
    for i in graph.stationsDict:
        count+=1
    
    return count

def numberConnections(graph):
    count = 0
    for node in graph.adj_list:
        for i in graph.adj_list[node]:
            count+=1
    
    return count

def numberDegreesperNode(graph):
    
    degreeLengthDict = {}

    for node in graph.adj_list:
        
        mappedNode = node.get_id()

        if mappedNode in degreeLengthDict: 
            degreeLengthDict[mappedNode] += len(graph.adj_list[node])
        else: 
            degreeLengthDict[mappedNode] = len(graph.adj_list[node])
        
        # print("node", mappedNode)
        
        for i in graph.adj_list[node]:
            
            connectingStation = i[0].get_id()

            if connectingStation in degreeLengthDict: 
                degreeLengthDict[connectingStation] += 1
            else: 
                degreeLengthDict[connectingStation] = 1
            
            # print("adj", connectingStation)

    return degreeLengthDict

def numberDegreesperStation(graph):
    
    degreesList = {}

    degreeLengthDict = numberDegreesperNode(graph)
    
    for i in degreeLengthDict:
        deg = degreeLengthDict[i]
        if deg in degreesList:
            degreesList[deg] += 1
        else:
            degreesList[deg] = 1
    
    return degreesList
    
def numberAvgDegree(graph):
    numDeg = sum(numberDegreesperNode(graph).values())
    return (numDeg / numberNodes(graph))

def plotNumberDegrees(graph):
    degreeLengthDict = numberDegreesperStation(graph)

    degreeKeys = list(degreeLengthDict.keys())
    degreeValues = list(degreeLengthDict.values())

    plt.bar(degreeKeys, degreeValues)
  
    plt.xlabel('Degree of Nodes')
    plt.ylabel('Frequency')
    plt.title('Degree of Nodes vs Frequency')
    plt.show()
        
    return 
