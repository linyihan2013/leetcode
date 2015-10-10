__author__ = 'yihan'
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        i = 0
        while i < len(path):
            while i < len(path) and path[i] == '/':
                i += 1
            if i is len(path):
                break
            start = i
            while i < len(path) and path[i] != '/':
                i += 1
            end = i
            element = path[start:end]
            if element == "..":
                if len(stack):
                    stack.pop(-1)
            elif element != "." and element != "":
                stack.append(element)
        if len(stack) is 0:
            return "/"
        Path = ""
        for i in stack:
            Path += "/" + i
        return Path