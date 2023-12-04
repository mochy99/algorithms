from test import test
from convertArray import convertArray
def maxIS(fileName):
    path = [0]
    path.extend(convertArray(fileName))
    graph = path[:]
    n = len(path) 
    print(n)
    setNode, weight, i = [], 0, n - 1
    for index in range(2,n):
        path[index] = max(path[index-1], path[index-2] + path[index])
    
    while i >= 2:
        if path[i-1] >= path[i-2] + graph[i]:
            i -= 1
        else:
            setNode.append(i)
            i -= 2
    if i == 1:
        setNode.append(i)
  
    return setNode, path[n-1]

testCase1=maxIS('testCase/IS1.txt')
print(testCase1)

