# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        ver = 0
        while low < high:
            ver = low + (high - low) / 2
            if isBadVersion(ver):
                high = ver
            else:
                low = ver + 1
        return low