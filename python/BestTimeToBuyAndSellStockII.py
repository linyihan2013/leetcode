__author__ = 'yihan'
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        len1 = len(prices)
        if len1 <= 1:
            return 0
        i = 0
        res = 0
        while i < len1:
            while i < len1 - 1 and prices[i] > prices[i + 1]: i += 1
            start = i
            i += 1
            while i < len1 and prices[i] > prices[i - 1]: i += 1
            end = i - 1
            res += prices[end] - prices[start]
        return res