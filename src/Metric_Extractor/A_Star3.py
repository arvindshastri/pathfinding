from Strategy import Strategy
from OutputHelpers import *

class A_Star(Strategy):

    def get_heuristic(self, station1, station2):

        lat1 = float(station1.get_latitude())
        lon1 = float(station1.get_longitude())
        lat2 = float(station2.get_latitude())
        lon2 = float(station2.get_longitude())

        dlon = lon1 - lon2
        dlat = lat1 - lat2

        distance = dlat*dlat + dlon*dlon

        return distance

    def get_minimum(self, unvisited):
        F_SCORE = 1
        min = float('infinity')
        tempNode = None
        for node in unvisited:
            if unvisited[node][F_SCORE] < min:
                min = unvisited[node][F_SCORE]
                tempNode = node
        
        return tempNode
    
    def do_algorithm(self, graph, start_node, target_node):
        # Declare the visited and unvisited lists as dictionaries
        G_SCORE = 0
        F_SCORE = 1
        PREVIOUS = 2
        visited = {} 
        unvisited = {}
        start_node = graph.stationsDict[start_node]
        target_node = graph.stationsDict[target_node]

        # Add and initialise every node to the unvisited list
        for node in graph.adj_list:
            # Initialise g-score and f-score to infinity
            # and the previous node to None
            unvisited[node] = [float('infinity'), float('infinity'), None]

        # Update the values for the start node in the unvisited list
        f_score_value = self.get_heuristic(start_node, target_node)
        unvisited[start_node] = [0, f_score_value, None]

        # Repeat until there are no more nodes in the unvisited list
        finished = False
        while finished == False:
            # Check if there are no more nodes left to evaluate
            if len(unvisited) == 0:
                finished = True
            else:
                # Return the unvisited node with the lowest f-score
                current_node = self.get_minimum(unvisited)

                # Check if the current node is the target node
                if current_node == target_node:
                    # Add the current node to the visited list
                    visited[current_node] = unvisited[current_node]
                    finished = True
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
                                unvisited[tempNode][F_SCORE] = new_g_score + self.get_heuristic(tempNode, target_node)
                                unvisited[tempNode][PREVIOUS] = current_node

                    # Add the current node to the visited list
                    visited[current_node] = unvisited[current_node]

                    # Remove the current node from the unvisited list
                    del unvisited[current_node]

        # Return the final visited list
        x = target_node
        pathList = []
        pathList.append(target_node.get_id())

        while True:
            x = visited[x][PREVIOUS] 
        
            if x == None:
                break
            pathList.append(x.get_id())

        pathList.reverse()
        return pathList