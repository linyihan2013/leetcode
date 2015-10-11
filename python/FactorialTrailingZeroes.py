__author__ = 'yihan'
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        mul, sum = n, 0
        while mul > 0:
            sum += int(mul / 5)
            mul = int(mul / 5)
        return sum