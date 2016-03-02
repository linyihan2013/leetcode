class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        len1 = len(prices)
        if len1 <= 1:
            return 0
        maxFromHead = [0]
        minPrice, maxProfit = prices[0], 0
        for i in range(1, len1):
            minPrice = min(minPrice, prices[i - 1])
            maxProfit = max(maxProfit, prices[i] - minPrice)
            maxFromHead.append(maxProfit)
        maxPrice = prices[len1 - 1]
        res = maxFromHead[len1 - 1]
        maxProfit = 0
        for i in range(len1 - 2, 0, -1):
            maxPrice = max(maxPrice, prices[i + 1])
            maxProfit = max(maxProfit, maxPrice - prices[i])
            res = max(res, maxFromHead[i- 1] + maxProfit)
        return res