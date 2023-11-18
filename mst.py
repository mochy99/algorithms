from convertArray import convertUndirectedGraph
from heap import pairHeapify, pairExtractMin, pairDelete
from test import test
def prim(fileName):
    setVertices, setEdges = convertUndirectedGraph(fileName)
    mst, heap = set(), []
    result = 0
    mst.add(1)

    for pair in setEdges.get(1):
        heap.append(pair)
        pairHeapify(heap)
    
    while len(mst) < len(setVertices):
        vertex, weight = pairExtractMin(heap)
        mst.add(vertex)
        result += weight
        newEdges = setEdges.get(vertex)

        for frontier, cost in newEdges:
            if frontier not in mst:
                curValue = pairDelete(heap, frontier)
                if curValue is None:
                    global minValue
                    minValue = cost
                else:
                    minValue = min(curValue, cost)
                heap.append((frontier,minValue))
                pairHeapify(heap)
    return result


case1 = prim("testcase/mst.txt")
print(test(1, case1, 14))
