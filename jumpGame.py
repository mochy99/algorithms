def jump(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        acc, n, step = 0, len(nums) - 1 , 0
        backup = []
        for i in range(n):
            if i + nums[i] >= n:
                n = i
                step +=1
                break
            if nums[i] > acc:
                print('jump')
                acc = nums[i]
                print("acc " + str(acc))
                step += 1
            acc -= 1
            print('nums[i] ' + str(nums[i]))
            print("i " + str(i))
            print("acc " + str(acc))
            print("step " + str(step))
        return step
            

            
array = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
result = jump(array)
print(result)