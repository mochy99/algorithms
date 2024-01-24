import random
from convertArray import convertArray
count = 0
def quickSort(input, start, end):
    if start >= end:
        return input

    i = swap(input, start, end)
    quickSort(input, start, i - 1)
    quickSort(input, i, end)
    return count

def swap(array, start, end):
    first = array[start]
    middle = array[(start + end -1) // 2]
    last = array[end-1]
    if first != min(first, middle, last) and first != max(first, middle, last):
        k = start
    elif last != min(first, middle, last) and last != max(first, middle, last):
        k = end -1
    else:
        k = (start + end -1) // 2
    pivot = array[k]
    array[start], array[k] = array[k], array[start]
    border = start + 1
    for index in range (start + 1, end):
        global count
        count += 1
        if array[index] < pivot:
            array[border], array[index] = array[index], array[border]
            border += 1
    array[start], array[border -1] = array[border -1], array[start]
    return border

# input_list = [3,4,2,1]
# sorted_list = quickSort(input_list, 0, len(input_list))
# print(sorted_list)  
array = convertArray('problem_set/course1/quickSort.txt')
print(quickSort(array, 0, len(array)))
# ans for 1st: 162085
# ans for last: 164123
# and for middle: 138382

