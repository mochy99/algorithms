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
           
            

def heap(array):
    n = len(array)
    heap = []
    for i in range(n):
        heap.append(array[i])
        low_heapify(heap)
        
    return heap

