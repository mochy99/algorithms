class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n= len(nums)
        if k > n:
            k = k % n
        newList = []
        for i in range(k - 1, -1, -1):
            newList.append(nums[n - i - 1])
        newList.extend(nums[: n - k])
        for i in range(n):
            nums[i] = newList[i]