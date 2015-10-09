__author__ = 'yihan'
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) <= 1:
            return True
        charMap = {}
        for i in s:
            if i not in charMap:
                charMap[i] = 1
            else:
                charMap[i] += 1
        tolerance = 0
        for i in charMap.keys():
            if charMap[i] % 2 != 0:
                tolerance += 1
        if len(s) % 2 == 0:
            return tolerance == 0
        else:
            return tolerance == 1
