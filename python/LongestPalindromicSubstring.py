class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length <= 1: return s
        start, maxSize = 0, 0
        for i in range(1, length):
            low, high = i - 1, i
            while low >= 0 and high < length and s[low] == s[high]:
                low -= 1
                high += 1
            if high - low - 1 > maxSize:
                maxSize = high - low - 1
                start = low + 1

            low, high = i - 1, i + 1
            while low >= 0 and high < length and s[low] == s[high]:
                low -= 1
                high += 1
            if high - low - 1 > maxSize:
                maxSize = high - low - 1
                start = low + 1
        return s[start: start+maxSize+1]