import string

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        splits = str.split(' ')
        map1 = {}
        len1 = len(splits)
        len2 = len(pattern)
        if len1 != len2:
            return False
        for i in range(len(pattern)):
            if pattern[i] not in map1:
                map1[pattern[i]] = splits[i]
            if splits[i] not in map1:
                map1[splits[i]] = pattern[i]
            if map1[pattern[i]] != splits[i] or map1[splits[i]] != pattern[i]:
                return False
        return True
