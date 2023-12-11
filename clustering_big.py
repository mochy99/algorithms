from convertArray import convertStrArray
from merge_sort import parallelMergeSort
from test import test

toggle = {"1": "0", "0": "1"}   

def find_k(fileName):
    # Initialize
    strs, dicEdge, leader, rank = convertStrArray(fileName)
    n = len(dicEdge)
    k = len(leader) - 1

    def join(fNode, sNode):
        fParent, sParent = find(leader, int(fNode)), find(leader, int(sNode))
        nonlocal k
        if k > 0:
            if fParent != sParent:
                k -= 1
                union(leader, rank, int(fNode), int(sNode))

    # Distance = 0
    for key in dicEdge:
        collectionNode = dicEdge[key]
        for i in range(len(collectionNode)):
            for j in range(i + 1, len(collectionNode)):
                join(collectionNode[i], collectionNode[j])

    # Distance = 1
    for key in dicEdge:
        collectionNode = dicEdge[key]
        for i in range(len(key)):
            toggled_value = key[:i] + toggle[key[i]] + key[i+1 :]
            if dicEdge.get(toggled_value):
                secondCollectionNode = dicEdge[toggled_value]
        
                for i in range(len(collectionNode)):
                    for j in range(len(secondCollectionNode)):
                        join(collectionNode[i], secondCollectionNode[j])

    # Distance = 2
    for key in dicEdge:
        collectionNode = dicEdge[key]
        for i in range(len(key)):
            for j in range(i+1, len(key)):
                new_value = key[:i] + toggle[key[i]] + key[ i+1 : j] + toggle[key[j]] + key[ j+1 :]
            
                if dicEdge.get(new_value):
                    secondCollectionNode = dicEdge.get(new_value)
                    for i in range(len(collectionNode)):
                        for j in range(len(secondCollectionNode)):
                            join(collectionNode[i], secondCollectionNode[j])
    print(k)
    return k

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

# Example usage

# testcase = find_k('testCase/clustering_big1.txt')
# print(test(1, testcase, 3))
# testcase1 = find_k('testCase/clustering_big2.txt')
# print(test(2, testcase1, 2))
ans = find_k('problem_set/course3/problem_2_week_2.txt')
print(ans)




