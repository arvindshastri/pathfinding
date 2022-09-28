from math import sin, cos, sqrt, atan2, radians
import pprint
from queue import PriorityQueue
import heapq

def heuristic(station1, station2):
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

def a_star_search(graph, start, goal):
    frontier = [(0, start)] 
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while len(frontier) > 0:
        current_priority, current = heapq.heappop(frontier)
        
        if current.get_id() == goal.get_id():
            break
        
        for next in graph.adj_list[current]:
            tempNode = next[0]
            new_cost = cost_so_far[current] + next[1].get_time()
            if tempNode not in cost_so_far or new_cost < cost_so_far[tempNode]:
                cost_so_far[tempNode] = new_cost
                priority = new_cost + heuristic(tempNode, goal)
                heapq.heappush(frontier, (priority, tempNode))
                came_from[tempNode] = current

    return came_from, cost_so_far


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

pprint.pprint(a_star_search(graph, graph.stationsDict['11'], graph.stationsDict['163']))
