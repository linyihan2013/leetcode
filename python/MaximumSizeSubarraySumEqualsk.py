import sys

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or len(nums) == 0: return 0
        map = {}
        map[0] = -1
        sum = 0
        maxLen = -sys.maxsize
        for i in range(len(nums)):
            sum += nums[i]
            if sum not in map:
                map[sum] = i
            if sum - k in map:
                index = map[sum - k]
                maxLen = max(maxLen, i - index)
        if maxLen == -sys.maxsize: return 0
        return maxLen