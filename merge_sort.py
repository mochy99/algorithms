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


def parallelMergeSort (org, indicator):
    n = len(indicator)
    if n <= 1:
        return org, indicator
    leftOrg, rightOrg = org[:n//2], org[n//2:]
    leftInd, rightInd = indicator[:n//2], indicator[n//2:]
    left_org, left_ind = parallelMergeSort(leftOrg, leftInd)
    right_org, right_ind = parallelMergeSort(rightOrg, rightInd)

    return parallelSort(left_org, left_ind, right_org, right_ind)

def parallelSort(left_org, left_ind, right_org, right_ind):
    result_org = []
    result_ind = []
    i, j = 0, 0
    while i < len(left_org) and j < len(right_org):
        if left_ind[i] > right_ind[j] or (left_ind[i] == right_ind[j] and left_org[i][0] > right_org[j][0]):
            result_org.append(left_org[i])
            result_ind.append(left_ind[i])
            i += 1
        else:
            result_org.append(right_org[j])
            result_ind.append(right_ind[j])
            j += 1

    result_org.extend(left_org[i:])
    result_ind.extend(left_ind[i:])
    result_org.extend(right_org[j:])
    result_ind.extend(right_ind[j:])

    return result_org, result_ind