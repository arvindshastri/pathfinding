import heapq
import pprint

def calculate_distances(graph, starting_vertex):
    distances = {vertex.get_id(): float('infinity') for vertex in graph.adj_list}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]  # distance, vertex

    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue
    
        station = graph.stationsDict[current_vertex]

        for neighbor, weight in graph.adj_list[station]:
            distance = current_distance + weight.get_time()

            # Only consider this new path if it's better than any path we've
            # already found.
            index = neighbor.get_id()

            if distance < distances[index]:
                distances[index] = distance
                heapq.heappush(pq, (distance, index))

    return distances

#TESTING BELOW

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

pprint.pprint(calculate_distances(graph, '11'))
