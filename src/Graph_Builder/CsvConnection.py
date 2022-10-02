import csv
from Connection import connectionBuilder


def csvReaderConnections(londonConnections, lines, stations):

    connections = []

    with open(londonConnections) as csvLines:
        reader = csv.reader(csvLines)
        next(reader)

        for row in reader:

            # extracting header info based on .csv format
            station1 = stations[row[0]]
            station2 = stations[row[1]]
            line = lines[row[2]]
            time = int(row[3])

            # creating bidirectional connections
            tempConnection1 = connectionBuilder(station1, station2, line, time)
            tempConnection2 = connectionBuilder(station2, station1, line, time)
            connections.append(tempConnection1)
            connections.append(tempConnection2)

    return connections
