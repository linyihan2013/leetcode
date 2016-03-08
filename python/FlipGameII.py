class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n, l = len(s), list(s)
        for i in range(n - 1):
            if l[i] == l[i + 1] == '+' and not self.canWin(s[:i] + '-' + s[i + 2:]):
                return True
        return False