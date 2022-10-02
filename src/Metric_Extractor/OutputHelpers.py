def output_helper(graph, pathList, threshold=0):

    infoList = []
    currentLine = ""
    count = 0

    while count < (len(pathList) - 1):

        x = graph.stationsDict[pathList[count]]
        y = graph.stationsDict[pathList[count+1]]

        potentialStations = []
        selectedStation = []

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

        if x is None:
            break
        pathList.append(x.get_id())

    pathList.reverse()
    return pathList


def calculateStations(infoList):
    return len(infoList)


def calculateTime(infoList):
    total = 0
    for row in infoList:
        total += row[3]
    return total


def prettyOutput(infoList):

    totalStations = calculateStations(infoList)
    totalTime = calculateTime(infoList)

    print("{: <20} {: <30} {: <20} {: <10}".format(
        "Stations", "Line", "Line Number", "Time"))
    print("---------------------------------------------------------------------------------")  # noqa: E501
    for row in infoList:
        print("{: <20} {: <30} {: <20} {: <10}".format(*row))
    print("\n")
    print("{: <20} {: <30} {: <20} {: <10}".format(
        "Total Stations:", totalStations, "Total Time:", totalTime))
    print("\n")
