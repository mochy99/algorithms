from convertArray import convertSchedule
from test import test
#mergsort
def mergeSort (org, indicator):
    n = len(indicator)
    if n <= 1:
        return org, indicator
    leftOrg, rightOrg = org[:n//2], org[n//2:]
    leftInd, rightInd = indicator[:n//2], indicator[n//2:]
    left_org, left_ind = mergeSort(leftOrg, leftInd)
    right_org, right_ind = mergeSort(rightOrg, rightInd)

    return sort(left_org, left_ind, right_org, right_ind)

def sort(left_org, left_ind, right_org, right_ind):
    result_org = []
    result_ind = []
    i, j = 0, 0
    while i < len(left_org) and j < len(right_org):
        if left_ind[i] > right_ind[j]:
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

def sumCompeletion (scheduleSort):
    accLength, sum = 0, 0
    for weight, length in scheduleSort:
        accLength += length
        sum +=  accLength * weight
    return sum


def GreedyRatio(input):
    ratio = []
    schedule = input.get('details')
    for weight, length in schedule:
        ratio.append(weight/length)
    
    #mergsort
    scheduleSort, ratioSort = mergeSort(schedule, ratio)
    return sumCompeletion(scheduleSort)

def GreedyDiff(input):
    ratio = []
    schedule = input.get('details')
    for weight, length in schedule:
        ratio.append(weight - length)
    
    #mergsort
    scheduleSort, ratioSort = mergeSort(schedule, ratio)
    return sumCompeletion(scheduleSort)
   
    
    

testCase1 = convertSchedule('testCase/schedule.txt')
case1 = GreedyRatio(testCase1)
case2 = GreedyDiff(testCase1)
print(test(1, case1, 67247))
print(test(2, case2, 68615))






