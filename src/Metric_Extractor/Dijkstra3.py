from Strategy import Strategy

class Dijkstra(Strategy):
    
    def do_algorithm(self, graph, start_node, target_node):
       
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
        
        x = target_node
        pathList = []
        pathList.append(target_node.get_id())

        while True:
            x = adj_node[x] 
        
            if x == None:
                break
            pathList.append(x.get_id())

        pathList.reverse()
        print("Dijkstra: ", pathList, "\n")
        return pathList