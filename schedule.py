from convertArray import convertSchedule
from merge_sort import parallelMergeSort
from test import test

def sumCompeletion (scheduleSort):
    accLength, sum = 0, 0
    for weight, length in scheduleSort:
        accLength += length
        sum += accLength * weight
    return sum


def GreedyRatio(input):
    ratio = []
    schedule = input.get('details')
    for weight, length in schedule:
        ratio.append(weight/length)
    
    #mergsort
    scheduleSort, ratioSort = parallelMergeSort(schedule, ratio)
    return sumCompeletion(scheduleSort)

def GreedyDiff(input):
    ratio = []
    schedule = input.get('details')
    for weight, length in schedule:
        ratio.append(weight - length)
    
    #mergsort
    scheduleSort, ratioSort = parallelMergeSort(schedule, ratio)
    return sumCompeletion(scheduleSort)
   
    
    

# testCase1 = convertSchedule('testCase/schedule.txt')
# case2 = GreedyDiff(testCase1)
# case1 = GreedyRatio(testCase1)

# print(case1)
# print(case2)
prob = convertSchedule('problem_set/course3/prob1week1.txt')
print(GreedyDiff(prob))
print(GreedyRatio(prob))






