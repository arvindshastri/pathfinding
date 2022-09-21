import pprint

from Station import csvReaderStations
from Line import csvReaderLines
from Connection import csvReaderConnections

tempLines = csvReaderLines()
tempStations = csvReaderStations()
tempConnections = csvReaderConnections(tempLines, tempStations)
# pprint.pprint(tempLines)
# pprint.pprint(tempStations)
# pprint.pprint(tempConnections)

adj_list = {}
mylist = []
def add_station(station): #equivalent to adding nodes into existence
  if station not in mylist:
    mylist.append(station)
  else:
    print("Station ",station.get_name()," already exists!")
 
def add_line(connection): #equivalent to adding edges into existence
  temp = []
  connectionInfo = connection.get_information()
  station1 = connection.get_station1()
  station2 = connection.get_station2()
  if station1 in mylist and station2 in mylist: #checking if two stations are valid
    if station1 not in adj_list:            #key doesnt exist yet
      temp.append([station2,connectionInfo])
      adj_list[station1] = temp
   
    elif station1 in adj_list:
      temp.extend(adj_list[station1])
      temp.append([station2,connectionInfo])
      adj_list[station1] = temp
       
  else:
    print("Stations don't exist!")
 
def graph():
    for node in adj_list:
        print(node, " ---> ", [i for i in adj_list[node]])
    



for station in tempStations:
    add_station(station)

for connection in tempConnections:
    add_line(connection)

graph()
print(adj_list)
