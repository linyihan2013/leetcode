# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
def knows(a, b):
    return True

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        bitmap = [0] * n

        for i in range(n):
            for j in range(n):
                if i == j: continue

                if bitmap[j] >= 0:
                    if knows(i, j):
                        bitmap[i] = -1
                        bitmap[j] += 1
                    else:
                        bitmap[j] = -1

        for i in range(n):
            if bitmap[i] == n - 1:
                for j in range(n):
                    if i == j: continue
                    if knows(i, j): return -1
                return i
        return -1