from convertArray import convertDirectedGraph
from test import test
import sys

def floydMarshall(fileName):
    # Initialization
    setVertices, setEdges = convertDirectedGraph(fileName)
    n = len(setVertices)
    track = [[0 for _ in range(n+1)] for _ in range(n+1)]
    result = sys.maxsize
    for i in range(1, n + 1 ):
        for j in range(1, n + 1 ):
            track[i][j]= sys.maxsize
            if i == j:
                track[i][j]= 0
            if i in setEdges:

                for head, weight in setEdges[i]:
                    if j == head:
                        track[i][j]= weight
    
    # Main loop
    for k in range(1, n):
        newTrack = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(1, n + 1 ):
            for j in range(1, n + 1 ):
                path = min(track[i][j], (track[i][k] + track[k][j]))
                result = min(path, result)
                newTrack[i][j] = path
        
        track = newTrack[:]

    # Detect negative cycle
    for i in range(n+1):
        if track[i][i] != 0:
            return "Negative cycle"
    return result


testCase1 = floydMarshall("testCase/apsp1.txt")
testCase2 = floydMarshall("testCase/apsp2.txt")
print(test(1, testCase1, -2))
print(test(2, testCase2, "Negative cycle"))
# print(floydMarshall("problem_set/course4/g1week1.txt"))

