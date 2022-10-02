import sys
import pprint

def output_helper(graph, pathList):
    
    infoList = []
    currentLine = ""
    count = 0

    while count < (len(pathList) - 1):

        x = graph.stationsDict[pathList[count]]
        y = graph.stationsDict[pathList[count+1]]

        potentialStations = []
        selectedStation = []
        threshold = 3
        
        min = float('infinity')
        
        for i in graph.adj_list[x]:
            if i[0] == y:
                if i[1].get_time() <= min + threshold:
                    min = i[1].get_time()
                    potentialStations.append(i)
            
        for i in potentialStations:
            if currentLine == i[1].get_line().get_name():
                selectedStation = i
        if len(selectedStation) == 0:
            selectedStation = i

        
        string = "{0} --> {1}".format(x.get_id(), y.get_id())
        lineName = selectedStation[1].get_line().get_name()
        lineID = selectedStation[1].get_line().get_line()
        time = selectedStation[1].get_time()
        currentLine = lineName
        infoList.append([string, lineName, lineID, time])
        count += 1
    
    return infoList


def pathList(visited, target_node):

    x = target_node
    pathList = []
    pathList.append(target_node.get_id())

    while True:
        x = visited[x] 
    
        if x == None:
            break
        pathList.append(x.get_id())

    pathList.reverse()
    return pathList

def calculateTime(infoList):
    total = 0
    for row in infoList:
        total += row[3]
    return total

def prettyOutput(infoList):    
    
    total = calculateTime(infoList)

    print("{: <20} {: <30} {: <20} {: <10}".format("Stations", "Line", "Line Number", "Time"))
    print("---------------------------------------------------------------------------------")
    for row in infoList:
        print("{: <20} {: <30} {: <20} {: <10}".format(*row))
    print("\n")
    print("{: <20} {: <30} {: <20} {: <10}".format("", "", "Total Time:", total))
    print("\n")

def dijkstra(graph, start_node, target_node):

    path = {}
    adj_node = {}
    queue = []
    start_node = graph.stationsDict[start_node]
    target_node = graph.stationsDict[target_node]

    for node in graph.adj_list:
        path[node.get_id()] = float("inf")
        adj_node[node] = None
        queue.append(node)
        
    path[start_node.get_id()] = 0

    while queue:
        # find min distance which wasn't marked as current
        key_min = queue[0] #station object
        min_val = path[key_min.get_id()] #int value
        
        for n in range(1, len(queue)):
            if path[queue[n].get_id()] < min_val: #int value < int value
                key_min = queue[n]  #object becomes object
                min_val = path[key_min.get_id()] #val becomes val
        cur = key_min
        queue.remove(cur) #obj
        
        for i in graph.adj_list[cur]:
            alternate = i[1].get_time() + path[cur.get_id()]
            if path[i[0].get_id()] > alternate:
                path[i[0].get_id()] = alternate
                adj_node[i[0]] = cur
    

    # pathListTemp = pathList(adj_node, target_node)
    # #print(pathListTemp)

    # infoListTemp = output_helper(graph, pathListTemp)
    # #pprint.pprint(infoListTemp)
    
    # prettyOutput(infoListTemp)

    x = target_node
    pathList = []
    pathList.append(target_node.get_id())

    while True:
        x = adj_node[x] 
    
        if x == None:
            break
        pathList.append(x.get_id())

    pathList.reverse()
    print(pathList)

#sys.path.insert(1, '../../src/Graph Builder') #running
sys.path.insert(0, './src/Graph Builder') #debugging

from CsvLine import csvReaderLines
from CsvStation import csvReaderStations
from CsvConnection import csvReaderConnections
from GraphBuilder import GraphBuilder

# londonLines = "./../../_dataset/london.lines.csv"
# londonStations = "./../../_dataset/london.stations.csv"
# londonConnections = "./../../_dataset/london.connections.csv"

londonLines = "_dataset/london.lines.csv"
londonStations = "_dataset/london.stations.csv"
londonConnections = "_dataset/london.connections.csv"

tempStations = csvReaderStations(londonStations)
tempLines = csvReaderLines(londonLines)
tempConnections = csvReaderConnections(londonConnections, tempLines, tempStations)

graph = GraphBuilder(tempStations, tempLines, tempConnections)
graph.load_graph()
