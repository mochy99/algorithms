def jump(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        step = 0
        n = len(nums) - 1
        while n > 0:
            for i in range(n):
                if i + nums[i] >= n:
                    n = i
                    step += 1
                    break
        return step
            

            
array = [2,3,0,1,4]
result = jump(array)
print(result)