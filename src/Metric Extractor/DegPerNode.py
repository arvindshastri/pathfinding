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