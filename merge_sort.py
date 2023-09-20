#input: the array is not sorted out
#output: the sorted array
def merge_sort(array):
    n2 = len(array) // 2
    l, r = array[:n2], array[n2:]
    if len(l) == 0 or len(r) == 0:
        return l or r
    return merge (merge_sort(l),merge_sort(r))

def merge(first, second):
    result = []
    j = 0
    i = 0
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1

    result.extend(second[j:]) 
    result.extend(first[i:])
    return result

array1 = [4,5,2,6,8,1,7]
print(merge_sort(array1))