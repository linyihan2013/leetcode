class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        i = cnt = 0
        known_sum = 1
        while known_sum <= n:
            if i < len(nums) and nums[i] <= known_sum:
                known_sum += nums[i]
                i += 1
            else:
                known_sum <<= 1
                cnt += 1
        return cnt