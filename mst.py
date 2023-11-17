from convertArray import convertUndirectedGraph
from test import test
import sys
def prim(fileName):
    setVertices, setEdges = convertUndirectedGraph(fileName)
    mst = set()
    result = 0
    mst.add(1)

    while len(mst) < len(setVertices):
        min = sys.maxsize
        global nextNode
        nextNode = None
        for vertex in mst:
            for frontier, weight in setEdges.get(vertex):
                if frontier not in mst:
                    if weight < min:
                        min = weight
                        nextNode = frontier
        mst.add(nextNode)
        result += min
    return result

case1 = prim("testcase/mst.txt")
print(test(1, case1, 14))