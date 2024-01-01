from convertArray import convertTsp
import math
import sys

def tsp(fileName):
    setVertices, data = convertTsp(fileName)
    def Euclidean(i,j):
        xi, yi = data[i]
        xj, yj = data[j]
        return math.sqrt((xj - xi)**2 + (yj - yi)**2)
    n = len(data)
    subset = {}
    prev = [None] * (n+1)
    for size in range(2, n+1):
        subset[size] = []
    
    # Generate all subsets having size greater than 1
    for i in range(2**n):
        current_subset = set()  
        for j in range(n):
            if (i & (1 << j)) > 0:
                current_subset.add(setVertices[j])
        if len(current_subset) > 1: # Only need subset having size greater than 1
            if 1 in current_subset: # Only need subset including 1
                size = len(current_subset)
                subset[size].append(current_subset)
                
    # Assign value for base case
    for curSet in  subset[2]:
        i,j = curSet
        distance =  Euclidean(i,j)
        if i == 1:
            prev[j] = distance
        else:
            prev[i] = distance
    print(prev)
    # Systematically solve all subproblems
    for size in range(3, n):
        tem = [None] * (n+1)
        for curSet in subset[size]:
            for j in curSet:
                if j != 1:
                    curMin = sys.maxsize
                    for k in curSet:
                        if k != 1 and k != j:
                            if j not in curSet:
                                curMin = min(curMin, 1)
                            

    





    return subset


# print(tsp('problem_set/course4/tsp.txt'))
print(tsp('testCase/tsp.txt'))

