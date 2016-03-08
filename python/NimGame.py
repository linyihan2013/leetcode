class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = n % 4
        if n == 0: return False
        return True