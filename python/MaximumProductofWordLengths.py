class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        elements = [0] * n
        for i , word in enumerate(words):
            for w in word:
                elements[i] |= 1 << (ord(w) - ord('a'))
        l = 0
        for i in range(n):
            for j in range(i + 1, n):
                if not elements[i] & elements[j]:
                    l = max(l, len(words[i]) * len(words[j]))
        return l