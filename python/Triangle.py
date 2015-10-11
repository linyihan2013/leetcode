__author__ = 'yihan'
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        sums = []
        for i in range(len(triangle)):
            tmp = []
            for j in range(len(triangle[i])):
                if i == 0:
                    tmp.append(triangle[i][j])
                else:
                    if j == 0:
                        tmp.append(triangle[i][j] + sums[i - 1][j])
                    elif j == i:
                        tmp.append(triangle[i][j] + sums[i - 1][j - 1])
                    else:
                        tmp.append(triangle[i][j] + min(sums[i - 1][j - 1], sums[i - 1][j]))
            sums.append(tmp)
        minSum = 0xfffffff
        for i in range(len(sums[-1])):
            minSum = min(minSum, sums[-1][i])
        return minSum