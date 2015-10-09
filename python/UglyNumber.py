__author__ = 'yihan'
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num >= 2:
            if num % 2 == 0:
                num /= 2
            elif num % 3 == 0:
                num /= 3
            elif num % 5 == 0:
                num /= 5
            else:
                return False
        return num == 1

    def nthUglyNumber(self, n):
        q = [1]
        i2 = i3 = i5 = 0
        while len(q) < n:
            m2, m3, m5 = q[i2] * 2, q[i3] * 3, q[i5] * 5
            m = min(m2, m3, m5)
            if m == m2:
                i2 += 1
            if m == m3:
                i3 += 1
            if m == m5:
                i5 += 1
            q += m
        return q[-1]
