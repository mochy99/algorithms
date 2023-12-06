from heap import pairExtractMin, pairHeapify
from convertArray import convertHuffMan
from test import test
import sys
def huffMan(fileName):
    tree, heapPa, deep = convertHuffMan(fileName)
    Max, Min = 1, sys.maxsize
    while len(tree) > 2:
        fNode, fProb = pairExtractMin(heapPa)

        sNode, sProb = pairExtractMin(heapPa)
       
        newNode, newProb = str(fNode) + "-" + str(sNode), fProb + sProb
        tree.remove(fNode)
        tree.remove(sNode)
        tree.add(newNode)

        heapPa.append((newNode,newProb))
        pairHeapify(heapPa)
        
        fDeepMax,fDeepMin = deep[fNode]
        sDeepMax, sDeepMin = deep[sNode]
        fUpMax,fUpMin, sUpMax, sUpMin= fDeepMax + 1,fDeepMin + 1, sDeepMax + 1, sDeepMin + 1
        deep.pop(fNode)
        deep.pop(sNode)
     
        deep[newNode] = (max(fUpMax, sUpMax), min(fUpMin, sUpMin))
       
        
    for node in deep:
        Max = max(Max,deep[node][0] +1)
        Min = min(Min,deep[node][1] +1)
    return Max, Min
        

testCase1 = huffMan('testCase/huffman1.txt')
print(test(1, testCase1, (3,2)))
testCase3 = huffMan('testCase/huffman3.txt')
print(test(3, testCase3, (6,3)))
testCase2 = huffMan('testCase/huffman2.txt')
print(test(2, testCase2, (5,2)))
ans = (huffMan("problem_set/course3/problem_1_week_3.txt"))
print(ans)