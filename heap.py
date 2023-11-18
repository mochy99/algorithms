#input: un ordered array
#ouput: heap array (min and/or max) *min
array = [9,8,7,6,5,4,3,2,1]
def low_heapify(array):
    n = len(array)
    if n > 1:
        self = n - 1
        parent = ((self + 1)// 2) - 1
        
        while array[self] < array[parent]:
            array[self], array[parent] = array[parent], array[self]
            if parent != 0:
                self = parent
                parent = ((self + 1)// 2) - 1

def high_heapify(array):
    n = len(array)
    if n > 1:
        self = n - 1
        parent = ((self + 1)// 2) - 1
        
        while array[self] > array[parent]:
            array[self], array[parent] = array[parent], array[self]
            if parent != 0:
                self = parent
                parent = ((self + 1)// 2) - 1
           
            

#input: min Heap
#output: return min and remaintain the heap
heap = [5, 6, 8, 9, 7]
def extractMin(arr):
    result = arr[0]
    arr[0] = arr.pop()
    n = len(arr)
    self = 0
    l = (self + 1) * 2 - 1
    r = (self + 1) * 2
    while (l < n and r < n and (arr[self] > arr[l] or arr[self] > arr[r])):
        if arr[l] < arr[r]:
            arr[self], arr[l] = arr[l], arr[self]
            self = l
        else:
            arr[self], arr[r] = arr[r], arr[self]
            self = r
        l = (self + 1) * 2 - 1
        r = (self + 1) * 2 
    return result
def extractMax(arr):
    result = arr[0]
    arr[0] = arr.pop()
    n = len(arr)
    self = 0
    l = (self + 1) * 2 - 1
    r = (self + 1) * 2
    while (l < n and r < n and (arr[self] < arr[l] or arr[self] < arr[r])):
        if arr[l] > arr[r]:
            arr[self], arr[l] = arr[l], arr[self]
            self = l
        else:
            arr[self], arr[r] = arr[r], arr[self]
            self = r
        l = (self + 1) * 2 - 1
        r = (self + 1) * 2 
    return result

#------------------------------
# handle with pair (key, value)
exp = [(5, 0), (6, 1), (2, 3), (4, 5), (5, 9)]
def pairHeapify(array):
    n = len(array)
    child = n - 1
    parent = (child + 1) // 2 - 1
    while array[parent][1] > array[child][1]:
        array[parent], array[child] = array[child], array[parent]
        if parent > 0:
            child = parent
            parent = (child + 1) // 2 - 1


def pairExtractMin(array):
    minResult = array[0]
    array[0] = array.pop()
    n = len(array)
    parent  = 0
    l, r = (parent + 1 ) * 2 - 1, (parent + 1) * 2
    while l < n and r < n and (array[parent][1] > array[l][1] or array[parent][1] > array[r][1]):
        if array[parent][1] > array[l][1]:
            array[parent], array[l] = array[l], array[parent]
            parent = l
        else:
            array[parent], array[r] = array[r], array[parent]
            parent = r
        l, r = (parent + 1 ) * 2 - 1, (parent + 1) * 2
    return minResult

def pairDelete(array, item):
    for i in range(len(array)):
        key = array[i][0]
        if key == item:
            global parent
            parent = i
            break
    array[parent] = array.pop()
    n = len(array)
    l, r = (parent + 1 ) * 2 - 1, (parent + 1) * 2
    while l < n and r < n and (array[parent][1] > array[l][1] or array[parent][1] > array[r][1]):
        if array[parent][1] > array[l][1]:
            array[parent], array[l] = array[l], array[parent]
            parent = l
        else:
            array[parent], array[r] = array[r], array[parent]
            parent = r
        l, r = (parent + 1 ) * 2 - 1, (parent + 1) * 2
