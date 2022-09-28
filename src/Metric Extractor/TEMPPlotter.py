import matplotlib.pyplot as plt    

def plotDegreeFrequency(graph):
    degreeLengthDict = numberOfDegreesPerStation(graph)

    degreeKeys = list(degreeLengthDict.keys())
    degreeValues = list(degreeLengthDict.values())

    plt.bar(degreeKeys, degreeValues)
  
    plt.xlabel('Degree of Nodes')
    plt.ylabel('Frequency')
    plt.title('Degree of Nodes vs Frequency')
    plt.show()
        
    return 
