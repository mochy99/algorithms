from convertArray import convertTsp
import math
import sys

def tsp(fileName):
    # Declare variables
    setVertices, data = convertTsp(fileName)
    lastRound = ''
    result, path = sys.maxsize, ''
    n = len(data)
    subset = {}
    prev = {}
    for size in range(2, n+1):
        subset[size] = []

    # Helper function
    def Euclidean(i,j):
        xi, yi = data[i]
        xj, yj = data[j]
        return math.sqrt((xj - xi)**2 + (yj - yi)**2)
    def toString(subSet):
        string = ''
        for item in subSet:
            string += str(item)
        return string
    def toStringNotIncludedJ(subSet, j):
        string = ''
        for item in subSet:
            if item != j:
                string += str(item)
        return string
   
    
    # Generate all subsets having size greater than 1
    for i in range(2**n):
        current_subset = []
        for j in range(n):
            if (i & (1 << j)) > 0:
                current_subset.append(setVertices[j])
        if len(current_subset) > 1: # Only need subset having size greater than 1
            if 1 in current_subset: # Only need subset including 1
                size = len(current_subset)
                subset[size].append(current_subset)
                
    # Assign value for base case
    for curSet in  subset[2]:
        i,j = curSet
        curSet = toString(curSet)
        distance =  Euclidean(i,j)
        prev[curSet] = [sys.maxsize] * (n+1)
        if i == 1:
            prev[curSet][j] = (distance, str(j))
        else:
            prev[curSet][i] = (distance, str(i))
    
    # Systematically solve all subproblems
    for size in range(3, n+1):
        tem = {}
        for curSet in subset[size]:
            if size == n:
                lastRound = toString(curSet)
            tem[toString(curSet)] = [sys.maxsize] * (n+1)
            for j in curSet:
                if j != 1:
                    curMin = sys.maxsize
                    for k in curSet:
                        if k != 1 and k != j:
                            subSetNotj = toStringNotIncludedJ(curSet, j)
                            curValue, path = prev[subSetNotj][k]
                            if curValue < curMin:
                                curMin =  curValue + Euclidean(k,j)
                                tem[toString(curSet)][j] = (curMin, path + str(j))
        prev = {}
        prev = tem

    for i in range(2, len(prev[lastRound])):
        value, curPath = prev[lastRound][i]
        newValue = value + Euclidean(1,i)
        if newValue < result:
            result = newValue
            path = curPath + str(1) 
    
    return result, path

                            



# print(tsp('problem_set/course4/tsp.txt'))
print(tsp('testCase/tsp.txt'))

