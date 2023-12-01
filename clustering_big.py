from convertArray import convertStrArray
from merge_sort import parallelMergeSort
from test import test

collection, leader, rank = [], [None], [None]
def hamming_distance(str1, str2):

    return sum(bit1 != bit2 for bit1, bit2 in zip(str1, str2))

def find_pairs_with_hamming_distance_less_than_2(strings):
    collection, leader, rank = [], [None], [None]
    n = len(strings)
    collection0, collection1, collection2 = [], [], []
    for i in range(1,n):
        leader.append(i)
        rank.append(0)
        for j in range(i + 1, n):
            distance = hamming_distance(strings[i], strings[j])
            if distance == 0:
                collection0.append((i, j, distance))
            elif distance == 1:
                collection1.append((i, j, distance))
            elif distance == 2:
                collection2.append((i, j, distance))
    
    collection.extend(item for item in collection0)
    collection.extend(item for item in collection1)
    collection.extend(item for item in collection2)
    return collection, leader, rank 

def find_k(input):
    # Initialize
    collection, leader, rank = find_pairs_with_hamming_distance_less_than_2(convertStrArray(input))
    k = len(leader) - 1
    for fNode, sNode, weight in collection:
        fParent, sParent = find(leader, int(fNode)), find(leader, int(sNode))
        
        if k > 0:
            if fParent != sParent:
                k -= 1  
                union(leader, rank, int(fNode), int(sNode))

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
testcase = find_k('testCase/clustering_big1.txt')
print(test(1, testcase, 3))
testcase1 = find_k('testCase/clustering_big2.txt')
print(test(2, testcase1, 2))
ans = find_k('testCase/problem_2_week_2.txt')
print(ans)