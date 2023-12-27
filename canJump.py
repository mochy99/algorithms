def canJump(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        acc = 0 
        n = len(nums)
        for i in range(n):
            if i == n - 1:
                  return True
            acc += nums[i]
            if i + acc >= n - 1:
                return True
            elif acc == 0:
                return False
            else:
                acc -= 1

