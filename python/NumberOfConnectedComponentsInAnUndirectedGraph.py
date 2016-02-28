class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        class UnionFind(object):
            def __init__(self, num):
                self.ids = [x for x in range(num)]
                self.count = num

            def find(self, i):
                if self.ids[i] == i: return i
                self.ids[i] = self.find(self.ids[i])
                return self.ids[i]

            def getCount(self):
                return self.count

            def union(self, i1, i2):
                self.ids[self.find(i1)] = self.find(i2)

        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)
        s = set()
        for i in range(n):
            s.add(uf.find(i))
        return len(s)