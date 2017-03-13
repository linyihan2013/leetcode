class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        p1 = p2 = 0
        for p2 in range(l):
            if nums[p2]:
                nums[p2], nums[p1] = nums[p1], nums[p2]
                p1 += 1