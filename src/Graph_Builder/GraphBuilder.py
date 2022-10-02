class GraphBuilder():

    adj_list = {}
    nodeList = []

    def __init__(self, stationsDict, linesDict, connectionsList):
        self.stationsDict = stationsDict
        self.linesDict = linesDict
        self.connectionsList = connectionsList

    def get_stationsDict(self):
        return self.stationsDict

    # adding stations that are not already present within nodeList
    def add_station(self, station):
        inside = False
        for i in self.nodeList:
            if station.get_id() == i.get_id():
                inside = True

        if inside is False:
            self.nodeList.append(station)

    def add_line(self, connection):
        temp = []
        connectionInfo = connection.get_information()
        station1 = connection.get_station1()
        station2 = connection.get_station2()

        statement1 = any(node is station1 for node in self.nodeList)
        statement2 = any(node is station2 for node in self.nodeList)

        # if there are valid nodes within nodeList
        if statement1 and statement2:

            # if there are is no existing mapped node in adjacency list
            if not any(node is station1 for node in self.adj_list):
                temp.append([station2, connectionInfo])
                self.adj_list[station1] = temp

            else:
                temp.extend(self.adj_list[station1])
                temp.append([station2, connectionInfo])
                self.adj_list[station1] = temp

    def load_graph(self):
        # automates adding all stations and connections to graph
        for station in self.stationsDict.values():
            self.add_station(station)

        for connection in self.connectionsList:
            self.add_line(connection)

    def print_graph(self):
        for node in self.adj_list:
            tempNodePrint = node.get_id()
            tempList = []
            for i in self.adj_list[node]:
                tempList.append([i[0].get_id(), i[1].get_name()])

            print(tempNodePrint, " ---> ", tempList)
