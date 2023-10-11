import random

def quickSort(input, start, end):
    if start >= end:
        return input

    input, i = swap(input, start, end)
    quickSort(input, start, i - 1)
    quickSort(input, i + 1, end)
    return input

def swap(input, start, end):
    k = random.randint(start, end - 1)
    pivot = input[k]
    input[start], input[k] = input[k], input[start]
    i = start
    j = start
    while j < end:
        if input[j] < pivot:
            if i != start:
                input[i + 1], input[j] = input[j], input[i + 1]
            i = i + 1
        j = j + 1
    input[start], input[i] = input[i], input[start]
    return input, i

input_list = [2, 3, 1, 5, 4]
sorted_list = quickSort(input_list, 0, len(input_list) - 1)
print(sorted_list)
