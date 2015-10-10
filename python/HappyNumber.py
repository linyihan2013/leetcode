__author__ = 'yihan'
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        elif n == 1:
            return True
        numSet = set()
        while n != 1 and n not in numSet:
            numSet.add(n)
            sum = 0
            while n:
                tmp = n % 10
                sum += tmp * tmp
                n /= 10
            n = sum
        return n == 1
