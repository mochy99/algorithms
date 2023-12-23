def jump(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        acc, n, step = 0, len(nums) - 1 , 0

        for i in range(n):
            if i + nums[i] >= n:
                n = i
                step +=1
                break
            if nums[i] > acc:
                acc = nums[i]
                step += 1
            acc -= 1

        return step
            

            
array = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
result = jump(array)
print(result)