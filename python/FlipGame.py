class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        flips, n, s = [], len(s), list(s)
        for i in range(n - 1):
            if s[i] == s[i + 1] == '+':
                s[i] = s[i + 1] = '-'
                flips.append(''.join(s))
                s[i] = s[i + 1] = '+'
        return flips