from convertArray import convertHeuristicTsp
import math
import sys

def heuristicTSP(fileName):
    # Initilization
    setVertices, data = convertHeuristicTsp(fileName)
    curCity, path, result = setVertices[0], {setVertices[0]}, 0
    n = len(setVertices)
    # Helper
    def Euclidean(i,j):
        xi, yi = data[i]
        xj, yj = data[j]
        distance = math.sqrt((xj - xi)**2 + (yj - yi)**2)
        return distance
    
    def minDistance(city):
        minDistance, nextCity = sys.maxsize, 0
        for vertex in setVertices:
            distance = Euclidean(vertex, city)
            if city != vertex and vertex not in path and distance < minDistance:
                minDistance = distance
                nextCity = vertex
        return minDistance, nextCity
    # Main loop
    while len(path) < n:
        minDist , nextCity = minDistance(curCity)
        result += minDist
        path.add(nextCity)
        curCity = nextCity
    result += Euclidean(nextCity, 1)
    return result


print(heuristicTSP('problem_set/course4/heuristicTSP.txt')) # 561767.7901999226
# print(heuristicTSP('testCase/heuristicTSP.txt'))