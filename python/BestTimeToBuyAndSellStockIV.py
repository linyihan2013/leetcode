__author__ = 'yihan'
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        len1 = len(prices)
        if k >= len1:
            return self.solveMaxProfit(prices)
        g, l = [], []
        for i in range(k + 1):
            g.append(0)
            l.append(0)
        for i in range(len1 - 1):
            diff = prices[i + 1] - prices[i]
            for j in range(k, 0, -1):
                l[j] = max(g[j - 1] + max(diff, 0), l[j] + diff)
                g[j] = max(g[j], l[j])
        return g[k]

    def solveMaxProfit(self, prices):
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        return res