from Line import csvReaderLines
from Station import csvReaderStations
from Connection import csvReaderConnections
from GraphBuilder import GraphBuilder

londonLines = r"D:\MacYear3\3XB3\L1Graph\l1-graph-lab\_dataset\london.lines.csv"
londonStations = r"D:\MacYear3\3XB3\L1Graph\l1-graph-lab\_dataset\london.stations.csv"
londonConnections = r"D:\MacYear3\3XB3\L1Graph\l1-graph-lab\_dataset\london.connections.csv"

tempStations = csvReaderStations(londonStations)
tempLines = csvReaderLines(londonLines)
tempConnections = csvReaderConnections(londonConnections, tempLines, tempStations)

graph = GraphBuilder(tempStations, tempLines, tempConnections)
graph.load_graph()


initial = '11'
path = {}
adj_node = {}
queue = []

for node in graph.adj_list:
    path[node.get_id()] = float("inf")
    adj_node[node] = None
    queue.append(node)
    
path[initial] = 0

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
            
            
x = graph.stationsDict['193']

pathList = []
infoList = []
pathList.append(x.get_id())

while True:
    y = x #store node in temp Var (station 2)
    x = adj_node[x] # station 1
    if x is None:
        break

    for i in graph.adj_list[y]:
        if i[0] == x:
            infoList.append([y.get_id(), i[1].get_line().get_name(), i[1].get_time()])
    pathList.append(x.get_id())

pathList.reverse()
infoList.reverse()

print(pathList)
print(infoList)
