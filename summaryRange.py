def summaryRanges(nums):
        head, tail = 0, 0
        i = 1
        last = (len(nums) - 1)
        result = []
        while i < len(nums):
            tail = i
            
            if nums[i - 1] + 1!= nums[tail]:
                if head == tail - 1:
                    result.append(str(nums[head]))
                else:
                    result.append(str(nums[head]) + '->' + str(nums[tail -1]))
                head = i
            if i == last:
                if head == i:
                    result.append(str(nums[i]))
                else:
                    result.append(str(nums[head]) + '->' + str(nums[i]))
            i += 1
        return result

array1 = [0,2,3,4,6,8,9]
result = summaryRanges(array1)
print(result)