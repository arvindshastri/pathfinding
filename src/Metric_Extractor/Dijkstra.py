from Strategy import Strategy


class Dijkstra(Strategy):

    def do_algorithm(self, graph, start_node, target_node):

        # declare the visited and unvisited lists as dictionaries
        # queue is the priority queue
        path = {}
        adj_node = {}
        queue = []
        # declare the station objects correlating to the station IDs
        start_node = graph.stationsDict[start_node]
        target_node = graph.stationsDict[target_node]

        # add and initialise every node to the queue
        for node in graph.adj_list:
            path[node.get_id()] = float("inf")
            adj_node[node] = None
            queue.append(node)

        # update the values for the start node in the unvisited list
        path[start_node.get_id()] = 0

        # repeat algorithm until there are no more nodes in the queue
        while queue:
            # find min distance which wasn't marked as current
            key_min = queue[0]
            min_val = path[key_min.get_id()]

            # find node with minimum value in path and remove
            for n in range(1, len(queue)):
                if path[queue[n].get_id()] < min_val:
                    key_min = queue[n]
                    min_val = path[key_min.get_id()]
            cur = key_min
            queue.remove(cur)

            # check neighbouring nodes and add to path and adj_node if
            # the stored time is greater
            for i in graph.adj_list[cur]:
                alternate = i[1].get_time() + path[cur.get_id()]
                if path[i[0].get_id()] > alternate:
                    path[i[0].get_id()] = alternate
                    adj_node[i[0]] = cur

        # traverse visited list backwards to each previous node
        # append to pathList and reverse to get forward list
        x = target_node
        pathList = []
        pathList.append(target_node.get_id())

        while True:
            x = adj_node[x]

            if x is None:
                break
            pathList.append(x.get_id())

        pathList.reverse()

        # declare as Dijkstra and return
        print("Dijkstra: ", pathList, "\n")
        return pathList
