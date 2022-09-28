from math import sin, cos, sqrt, atan2, radians
import pprint

# Index values for g-score, f-score and previous node
G_SCORE = 0
F_SCORE = 1
PREVIOUS = 2

def get_heuristic(station1, station2):

    R = 6373.0
    lat1 = radians(float(station1.get_latitude()))
    lon1 = radians(float(station1.get_longitude()))
    lat2 = radians(float(station2.get_latitude()))
    lon2 = radians(float(station2.get_longitude()))

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R*c

def get_minimum(unvisited):
    min = float('infinity')
    tempNode = None
    for node in unvisited:
        if unvisited[node][F_SCORE] < min:
            min = unvisited[node][F_SCORE]
            tempNode = node
    
    return tempNode

def a_star(graph, start_node, target_node):
    
    # Declare the visited and unvisited lists as dictionaries
    visited = {} 
    unvisited = {}

    # Add and initialise every node to the unvisited list
    for node in graph.adj_list:
        # Initialise g-score and f-score to infinity
        # and the previous node to None
        unvisited[node] = [float('infinity'), float('infinity'), None]

    # Update the values for the start node in the unvisited list
    f_score_value = get_heuristic(start_node, target_node)
    unvisited[start_node] = [0, f_score_value, None]

    # Repeat until there are no more nodes in the unvisited list
    finished = False
    while finished == False:
        # Check if there are no more nodes left to evaluate
        if len(unvisited) == 0:
            finished = True
        else:
            # Return the unvisited node with the lowest f-score
            current_node = get_minimum(unvisited)

            # Check if the current node is the target node
            if current_node == target_node:
                # Add the current node to the visited list
                finished = True
                visited[current_node] = unvisited[current_node]
            else:
                # Get the current node's list of neighbours
                neighbours = graph.adj_list[current_node]

                # Repeat for each neighbour node in the neighbours list
                for node in neighbours:
                    # Check if the neighbour node has already been visited
                    if node[0] not in visited:
                        # Calculate the new g-score
                        new_g_score = unvisited[current_node][G_SCORE] + node[1].get_time()

                        tempNode = node[0]
                        # Check if the new g-score is less
                        if new_g_score < unvisited[tempNode][G_SCORE]:
                            # Update g-score, f-score and previous node
                            unvisited[tempNode][G_SCORE] = new_g_score
                            unvisited[tempNode][F_SCORE] = new_g_score + get_heuristic(tempNode, target_node)
                            unvisited[tempNode][PREVIOUS] = current_node

                # Add the current node to the visited list
                visited[current_node] = unvisited[current_node]

                # Remove the current node from the unvisited list
                del unvisited[current_node]

    # Return the final visited list

    for i in visited.keys():
        print(i.get_id())

    return visited


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

a_star(graph, graph.stationsDict['11'], graph.stationsDict['82'])

