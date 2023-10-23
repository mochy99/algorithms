import random
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


input_list = [2, 3, 1, 5, 4, 6, 9, 8, 7]
ithElement = randomSelection(input_list, 9)
print(ithElement) 
