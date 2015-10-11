__author__ = 'yihan'
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        flag = 0
        i = len(s) - 1
        result = ""
        while i >= 0:
            while i >= 0 and s[i] == ' ': i -= 1
            if i < 0: break
            start = i
            while i >= 0 and s[i] != ' ': i -= 1
            end = i
            element = s[end + 1:start + 1]
            if flag == 0:
                result += element
                flag = 1
            else:
                result += " " + element
        return result