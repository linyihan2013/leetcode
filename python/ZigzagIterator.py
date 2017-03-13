class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        l1, l2 = len(v1), len(v2)
        whoShort = 0
        self.totalLen = l1 + l2
        minLen, maxLen = 0, 0
        if l1 < l2:
            minLen, maxLen, whoShort = l1, l2, 0
        else:
            minLen, maxLen, whoShort = l2, l1, 1
        self.v = []
        for i in range(minLen):
            self.v.append(v1[i])
            self.v.append(v2[i])
        for i in range(minLen, maxLen):
            if whoShort == 0:
                self.v.append(v2[i])
            else:
                self.v.append(v1[i])
        self.nextIter = 0

    def next(self):
        """
        :rtype: int
        """
        if self.nextIter < self.totalLen:
            self.nextIter += 1
            return self.v[self.nextIter - 1]
        else:
            return None

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.nextIter < self.totalLen

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())