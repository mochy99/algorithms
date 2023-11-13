import random
from convertArray import convertArray #input file.text #output array
from test import test
def randomSelection(array, i):
    def selection(array, start, end, i):
        if start + 1 == end:
            return array[start]
        
        border = swap(array, start, end, i)
        if border == i:
            return array[border -1]
        elif border < i:
            return selection(array, border, end, i)
        else:
            return selection(array, start, border - 1, i)
    
    def swap(array, start, end, i):
        k = random.randint(start, end -1)
        pivot = array[k]
        array[start], array[k] = array[k], array[start]
        border = start + 1
        for index in range (start + 1, end):
            if array[index] < pivot:
                array[border], array[index] = array[index], array[border]
                border += 1
        array[start], array[border -1] = array[border -1], array[start]
  
        return border
        
    return selection(array, 0, len(array), i)

testCase1 = convertArray("testCase/random1.txt")
testCase2 = convertArray("testCase/random2.txt")
case1 = randomSelection(testCase1, 5)
case2 = randomSelection(testCase2, 50)
print(test(1, case1, 5469)) 
print(test(2, case2, 4715)) 
