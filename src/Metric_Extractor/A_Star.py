from Strategy import Strategy


class A_Star(Strategy):

    # F_Score defines G_score + heuristic result
    # G_score defines the weight of the connection
    # Previous defines the position of the node previously visited

    # heuristic defined by Pythagorean distance between stations
    # assuming they can be treated like points on a Cartesian plane
    def get_heuristic(self, station1, station2):

        lat1 = float(station1.get_latitude())
        lon1 = float(station1.get_longitude())
        lat2 = float(station2.get_latitude())
        lon2 = float(station2.get_longitude())

        dlon = lon1 - lon2
        dlat = lat1 - lat2

        distance = dlat*dlat + dlon*dlon

        return distance

    # returns node in unvisited list with minimum f_score
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

        # declare variables for readability
        G_SCORE = 0
        F_SCORE = 1
        PREVIOUS = 2

        # declare the visited and unvisited lists as dictionaries
        # unvisited will act as a priority queue
        visited = {}
        unvisited = {}

        # declare the station objects correlating to the station IDs
        start_node = graph.stationsDict[start_node]
        target_node = graph.stationsDict[target_node]

        # add and initialise every node to the unvisited list
        for node in graph.adj_list:
            # initialise g-score and f-score to infinity
            # and the previous node to None
            unvisited[node] = [float('infinity'), float('infinity'), None]

        # update the values for the start node in the unvisited list
        f_score_value = self.get_heuristic(start_node, target_node)
        unvisited[start_node] = [0, f_score_value, None]

        # repeat algorithm until there are no more nodes in the unvisited list
        finished = False
        while finished is False:
            # check if there are no more nodes left to evaluate, and exit loop
            if len(unvisited) == 0:
                finished = True
            else:
                # return the unvisited node with the lowest f-score
                current_node = self.get_minimum(unvisited)

                if current_node == target_node:
                    # add the current node to the visited list
                    visited[current_node] = unvisited[current_node]
                    finished = True
                else:
                    # get the current node's list of neighbours
                    neighbours = graph.adj_list[current_node]

                    # repeat for each neighbour node in the neighbours list
                    for connection in neighbours:
                        # check if the neighbour node has already been visited
                        if connection[0] not in visited:
                            # calculate the new g-score
                            new_g_score = unvisited[current_node][G_SCORE] \
                                + connection[1].get_time()

                            # accesses the station object from resulting list
                            tempNode = connection[0]

                            # check if new g-score is less than neighbour node
                            if new_g_score < unvisited[tempNode][G_SCORE]:
                                # Update g-score, f-score and previous node
                                unvisited[tempNode][G_SCORE] = new_g_score
                                unvisited[tempNode][F_SCORE] = new_g_score \
                                    + self.get_heuristic(tempNode, target_node)
                                unvisited[tempNode][PREVIOUS] = current_node

                    # Add the current node to the visited list
                    visited[current_node] = unvisited[current_node]

                    # Remove the current node from the unvisited list
                    del unvisited[current_node]

        # traverse visited list backwards to each previous node
        # append to pathList and reverse to get forward list
        x = target_node
        pathList = []
        pathList.append(target_node.get_id())

        while True:
            x = visited[x][PREVIOUS]

            if x is None:
                break
            pathList.append(x.get_id())

        pathList.reverse()

        # declare as A* and return
        print("A*: ", pathList, "\n")
        return pathList
