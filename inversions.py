#input: the array 
#output: the number of inversions
def inversions(array,count):
    n2 = len(array) // 2
    left, right = array[:n2], array[n2:]
    if len(array) == 1:
        return array, 0
    sorted_left, count_left = inversions(left,count)
    sorted_right, count_right = inversions(right,count)
    sorted_merge, count_total = inversion_count(sorted_left, sorted_right)
    total = count_total + count_left + count_right
    return sorted_merge, total

def inversion_count(left, right):
    result = []
    j = 0
    i = 0
    count = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]: 
            result.append(left[i])
            i += 1
        else:
            result.append(right[i])
            j += 1
            count += len(left) - i
    result.extend(left[i:])
    result.extend(right[j:])
    return result, count

array1 = [4,5,2,6,8,1,7]
sorted_array, count = inversions(array1,0)
print("Sorted Array:", sorted_array)
print("Inversion Count:", count)