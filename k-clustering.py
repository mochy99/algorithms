from convertArray import convertSetEdges
from merge_sort import parallelMergeSort
from test import test

def k_clurering(fileName, k):
    #Initilization
    setVetices, setEdges, setWeight = convertSetEdges(fileName)
    leader, rank = [None] * (len(setVetices) + 1), [None] * (len(setVetices) + 1)
    setEdges, setWeight = parallelMergeSort(setEdges, setWeight)
    cum = 0
    for vertex in setVetices:
        leader[vertex] = vertex
        rank[vertex] = 0
    #Main loop
    for fNode, sNode, cost in setEdges:
        fParent, sParent = find(leader, int(fNode)), find(leader, int(sNode))
        if cum < len(setVetices) - k:
            if fParent != sParent:
                cum += 1
                union(leader, rank, int(fNode), int(sNode))
        else:
            if fParent != sParent:  
                return int(cost)
    
def find(leader,node):
    if leader[node] == node:
        return node
    else:
        return find(leader, leader[node])

def union(leader, rank, fNode, sNode):
    fParent = find(leader,fNode)
    sParent = find(leader,sNode)
    
    if rank[fParent] > rank[sParent]:
        leader[sParent] = fParent
        leader[sNode] = fParent
    elif rank[fParent] == rank[sParent]:
        leader[sParent] = fParent
        rank[fNode] += 1
    else:
        leader[fParent] = sParent
        leader[fNode] = sParent

case1 = k_clurering('testCase/clustering1.txt', 2)
case2 = k_clurering('testCase/clustering1.txt', 4)
case3 = k_clurering('testCase/clustering2.txt', 4)
case4 = k_clurering('testCase/clustering3.txt', 2)
case5 = k_clurering('testCase/clustering3.txt', 3)
case6 = k_clurering('testCase/clustering3.txt', 4)
case7 = k_clurering('testCase/clustering4.txt', 3)
case8 = k_clurering('testCase/clustering4.txt', 2)
case9 = k_clurering('testCase/clustering5.txt', 2)
case10 = k_clurering('testCase/clustering5.txt', 3)
case11 = k_clurering('testCase/clustering5.txt', 4)

print(test(1, case1, 5))
print(test(2, case2, 3))
print(test(3, case3, 7))
print(test(4, case4, 5))
print(test(5, case5, 2))
print(test(6, case6, 1))
print(test(7, case7, 3))
print(test(8, case8, 5))
print(test(9, case9, 8))
print(test(10, case10, 4))
print(test(11, case11, 1))
