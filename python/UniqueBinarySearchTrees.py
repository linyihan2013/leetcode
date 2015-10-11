__author__ = 'yihan'
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        res = []
        res.append(1)
        res.append(1)
        for i in range(2, n + 1):
            tmp = 0
            for j in range(i):
                tmp += res[j] * res[i - j - 1]
            res.append(tmp)
        return res[n]