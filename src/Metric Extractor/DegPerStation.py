import DegPerNode

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
    