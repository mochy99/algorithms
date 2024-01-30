from convertArray import convertKnapSack
from test import test
def knapsack(fileName, budget):
    with open(fileName, "r") as file:
        lines = file.readlines()
    prev = [0] * (budget + 1)
    for i in range(1, len(lines)):
        value, size = map(int, lines[i].split())
        cur = []
        cur.extend(prev[:size])
        for i in range(size, budget + 1):
            if size <= i:
                cur.append(max(prev[i], prev[i - size] + value))
        prev = cur[:]
    return prev[budget]

# test1 = knapsack('problem_set/course3/prob1week4.txt', 10000)
# print(test(1,test1,2493893) )
# test2 = knapsack('testCase/knapsack1.txt', 6)
# print(test(2,test2, 8))

# test3 = knapsack('problem_set/course3/prob2week4.txt', 2000000) #4243395
# print(test3)

test4 = knapsack('problem_set/course3/prob1week4.txt', 10000)
print(test4)