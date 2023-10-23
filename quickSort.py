import random

def quickSort(input, start, end):
    if start >= end:
        return input

    i = swap(input, start, end)
    quickSort(input, start, i - 1)
    quickSort(input, i, end)
    return input

def swap(array, start, end):
    k = random.randint(start, end - 1)
    pivot = array[k]
    array[start], array[k] = array[k], array[start]
    border = start + 1
    for index in range (start + 1, end):
        if array[index] < pivot:
            array[border], array[index] = array[index], array[border]
            border += 1
    array[start], array[border -1] = array[border -1], array[start]
    return border

input_list = [3,4,2,1]
sorted_list = quickSort(input_list, 0, len(input_list))
print(sorted_list)  