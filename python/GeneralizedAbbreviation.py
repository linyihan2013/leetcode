class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        result = []
        cur = word
        num = len(word)
        result.append(cur)
        def helper(cur, idx):
            for i in range(idx, num):
                l = 1
                while l <= num and i + l - 1 < len(cur):
                    tmp = cur[:i] + str(l) + cur[i + l:]
                    result.append(tmp)
                    helper(tmp, i + len(str(l)) + 1)
                    l += 1
        helper(cur, 0)
        return result