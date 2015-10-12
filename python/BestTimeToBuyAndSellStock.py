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
        res = prices[1] - prices[0]
        minPrice = prices[0]
        for i in range(2, len1):
            minPrice = min(prices[i - 1], minPrice)
            res = max(res, prices[i] - minPrice)
        if res < 0:
            return 0
        return res