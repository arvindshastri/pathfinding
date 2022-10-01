class GraphBuilder():

    adj_list = {}
    mylist = []

    def __init__(self, stationsDict, linesDict, connectionsList):
        self.stationsDict = stationsDict
        self.linesDict = linesDict
        self.connectionsList = connectionsList

    def get_stationsDict(self):
        return self.stationsDict

    def add_station(self, station):  # equivalent to adding nodes into existence
        if station not in self.mylist:
            self.mylist.append(station)
        else:
            print("Station ", station.get_name(), " already exists!")

    def add_line(self, connection):  # equivalent to adding edges into existence
        temp = []
        connectionInfo = connection.get_information()
        station1 = connection.get_station1()
        station2 = connection.get_station2()

        if any(node is station1 for node in self.mylist) and any(node is station2 for node in self.mylist):  # if stations valid
            if not any(node is station1 for node in self.adj_list):
                temp.append([station2, connectionInfo])
                self.adj_list[station1] = temp

            else:
                temp.extend(self.adj_list[station1])
                temp.append([station2, connectionInfo])
                self.adj_list[station1] = temp

        else:
            print("Stations don't exist!")

    def load_graph(self):
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