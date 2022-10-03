def dijkstra(graph, start_node, target_node):

    path = {}
    adj_node = {}
    queue = []
    start_node = graph.stationsDict[start_node]
    target_node = graph.stationsDict[target_node]
    nodes_visited = 0

    for node in graph.adj_list:
        path[node.get_id()] = float("inf")
        adj_node[node] = None
        queue.append(node)

    path[start_node.get_id()] = 0

    while queue:

        key_min = queue[0]
        min_val = path[key_min.get_id()]

        for n in range(1, len(queue)):
            if path[queue[n].get_id()] < min_val:
                key_min = queue[n]
                min_val = path[key_min.get_id()]
        cur = key_min
        queue.remove(cur)

        for i in graph.adj_list[cur]:
            alternate = i[1].get_time() + path[cur.get_id()]
            if path[i[0].get_id()] > alternate:
                path[i[0].get_id()] = alternate
                adj_node[i[0]] = cur
                nodes_visited += 1

    return nodes_visited
