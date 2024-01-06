import random, sys
from convertArray import convertMinCutGraph

def kargerMinCut(fileName):
    setEdges = convertMinCutGraph(fileName)
    refuse = {}
    numNodes = len(setEdges)
    leader, rank = [], []
    count, result = 0, 0
    for i in range(numNodes+1):
        if i == 0:
            leader.append(None)
            rank.append(None)
        else:
            leader.append(i)
            rank.append(1)

    while numNodes - count > 2:
        randomNode = random.randint(1, numNodes-1)
        numEdges = len(setEdges[randomNode])
        randomEdge = random.randint(0,numEdges -1)
        head = setEdges[randomNode][randomEdge]
        if find(leader, randomNode) != find(leader, head):
            union(leader, rank, randomNode, head)
            count += 1
       
    for i in range(len(leader)):
        if i > 0:
            if leader[i] != find(leader, i):
                leader[i] = find(leader, i)
            if leader[i] in refuse:
                refuse[leader[i]].add(i)
            else:
                refuse[leader[i]]= {i}
    minSet = sys.maxsize    
    smallSet = set()       
    for sets in refuse:
        if len(refuse[sets]) < minSet:
            smallSet = refuse[sets]
    for node in smallSet:
        for anotherNode in setEdges[node]:
            if anotherNode not in smallSet:
                result += 1
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
        leader[sParent] = fParent
        leader[sNode] = fParent
    elif rank[fParent] == rank[sParent]:
        leader[sParent] = fParent
        rank[fNode] += 1
    else:
        leader[fParent] = sParent
        leader[fNode] = sParent

minCut = sys.maxsize
for i in range(250):
    minCut = min(minCut, (kargerMinCut('problem_set/course1/minCut.txt')))

print(minCut) #ans: 17