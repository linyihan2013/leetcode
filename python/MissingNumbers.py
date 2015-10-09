__author__ = 'yihan'
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        tmp = 0
        for i in nums:
            tmp |= 1 << i
        tmp2 = 1
        for i in range(len(nums) + 1):
            if (tmp & tmp2) == 0:
                return i
            tmp2 <<= 1
