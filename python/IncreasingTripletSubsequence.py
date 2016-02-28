class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x1 = x2 = 0x7fffffff
        for num in nums:
            if num <= x1:
                x1 = num
            elif num <= x2:
                x2 = num
            else:
                return True
        return False