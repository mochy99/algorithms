from convertArray import convertDirectedGraph
from test import test
import sys
from heap import pairExtractMin, pairHeapify

def bellmanFord(setVertices, setEdges, start):
    budget = len(setVertices)
    init, prev = [], set()
    # Initialize 
    prev.add(start)
    for vertex in setVertices:
        if vertex == start:
            init.append(0) 
        else:
            init.append(sys.maxsize) 

    # Main loop
    for i in range(budget):
        new_nodes = set()
        for tail in prev:
            if tail in setEdges:
                for head, weight in setEdges[tail]:
                    value = min(init[head], init[tail] + weight)
                    init[head] = value
                    new_nodes.add(head)
        prev.update(new_nodes)

    # Detect a negative cycle
    for tail in prev:
        if tail in setEdges:
            for head, weight in setEdges[tail]:
                value = min(init[head], init[tail] + weight)
                if init[head] != value:
                    return "A negative cycle"
                       
    return init



def johnson(fileName):
    setVertices, setEdges = convertDirectedGraph(fileName)
    result = sys.maxsize
    # Add new S -> G'
    newEdges = []
    for vertex in setVertices:
        newEdges.append((vertex, 0))
    setEdges[0] = newEdges
    setVertices.add(0)

    # Run Bellman-Ford on G' to create indicators or detecting negative cycle
    bellman = bellmanFord(setVertices, setEdges, 0)

    if bellman == "A negative cycle":
        return bellman
    # # Recalculate weight:
    # for tail in setEdges:
    #     newEdges=[]
    #     for head, weight in setEdges[tail]:
    #         newEdges.append((head, weight + bellman[tail] - bellman[head]))
    #     setEdges[tail] = newEdges
    # # Run Dijkstra algorithm
    # for start in setVertices:
    #     # Initialize
    #     visited = [start]
    #     track = {start: 0}
    #     heap = []
    #     headOfStart = set()
    #     for head, weight in setEdges[start]:
    #         heap.append((head,weight))
    #         pairHeapify(heap)
    #         headOfStart.add(head)

    #     for vertex in setVertices:
    #         if vertex not in headOfStart and vertex != 0 and vertex != start:
    #             heap.append((vertex,sys.maxsize))
            
    #     while heap:
    #         nextNode, minLen = pairExtractMin(heap)
    #         visited.append(nextNode)
    #         track[nextNode] = minLen
    #         result = min(minLen, result)
    # return result

# testCase1 = johnson("testCase/apsp1.txt")
# testCase2 = johnson("testCase/apsp2.txt")
# print(test(1, testCase1, -2))
# print(test(2, testCase2, "A negative cycle"))
print(johnson("problem_set/course4/g4week1.txt")) 