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
    arr[0] = arr.pop(len(arr)-1)
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
    arr[0] = arr.pop(len(arr)-1)
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


