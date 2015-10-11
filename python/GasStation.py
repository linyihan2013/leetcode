__author__ = 'yihan'
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        sum, total, k = 0, 0, 0
        for i in range(len(gas)):
            sum += gas[i] - cost[i]
            if sum < 0:
                k = i + 1
                sum = 0
            total += gas[i] - cost[i]
        if total < 0:
            return -1
        else:
            return k