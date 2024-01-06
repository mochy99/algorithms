from convertArray import convertArray

def twoSum(fileName, below, above):
    array = convertArray(fileName)
    result = 0
    for target in range(below, above + 1):
        contained = {}
        for num in array:
            complement = target - num
            if  complement in contained and num != complement:
                result += 1
                break
            else:
                contained[num] = complement
          
    return result


# print(twoSum('testCase/2sum.txt', 3, 10))
print(twoSum('problem_set/course2/2sum.txt',-10000,10000)) #ans: 427