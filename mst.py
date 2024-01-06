from convertArray import convertUndirectedGraph, convertSetEdges
from heap import pairHeapify, pairExtractMin, pairDelete
from merge_sort import parallelMergeSort
from test import test
import sys
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



def krusal(fileName):
    #Initilization
    setVetices, setEdges, setWeight = convertSetEdges(fileName)
    leader, rank = [None] * (len(setVetices) + 1), [None] * (len(setVetices) + 1)
    result = 0
    setEdges, setWeight = parallelMergeSort(setEdges, setWeight)
    for vertex in setVetices:
        leader[vertex] = vertex
        rank[vertex] = 0
    for fNode, sNode, cost in setEdges:
        fParent, sParent = find(leader, int(fNode)), find(leader, int(sNode))
        
        if fParent != sParent:
            result += int(cost)
            union(leader, rank, int(fNode), int(sNode))
    
    return result

def find(leader,node):
    if leader[node] == node:
        return node
    else:
        return find(leader, leader[node])

def union(leader, rank, fNode, sNode):
    fParent = find(leader,fNode)
    sParent = find(leader,sNode)
    if rank[fParent] > rank[sParent]:
        leader[sNode] = fParent
    elif rank[fParent] == rank[sParent]:
        leader[sNode] = fNode
        rank[fNode] += 1
    else:
        leader[fNode] = sParent

def primWithoutHeap(fileName):
    setVertices, setEdges = convertUndirectedGraph(fileName)
    mst, cost = {1}, 0

    while len(mst) < len(setVertices):
        nextNode, minWeight = "None", sys.maxsize
        for tail in mst:
            for head, weight in setEdges[tail]:
                if weight < minWeight and head not in mst:
                    nextNode = head
                    minWeight = weight
        mst.add(nextNode)
        cost += minWeight
    return cost



# case1 = prim("testcase/mst.txt")
# case2 = krusal("testcase/mst.txt")
# print(case2)
# print(test(1, case1, 14))
# print(test(2, case2, 14))
print(primWithoutHeap('problem_set/course3/prob3week1.txt'))
# print(primWithoutHeap('testCase/mst2.txt'))
# print(prim('testCase/mst2.txt'))