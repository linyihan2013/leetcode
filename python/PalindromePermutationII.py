__author__ = 'yihan'

class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        palindromes = []
        counts = {}
        half = ""
        for i in s:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1
        odd = 0
        for i in counts.keys():
            if counts[i] & 1:
                odd += 1
                mid = i
                if odd > 1:
                    return palindromes
            for j in range(int(counts[i] / 2)):
                half += i
        palindromes = self.permutation(half)
        for i in range(len(palindromes)):
            t = palindromes[i][::-1]
            if odd:
                t = mid + t
            palindromes[i] += t
        return palindromes

    def nextPermutation(self, num):
        if len(num) <= 1: return num
        partition = -1
        for i in range(len(num)-2, -1, -1):
            if num[i] < num[i+1]:
                partition = i
                break
        if partition == -1:
            return num[::-1]
        else:
            for i in range(len(num)-1, partition, -1):
                if num[i] > num[partition]:
                    lst  = list(num)
                    lst[i], lst[partition] = lst[partition], lst[i]
                    num = ''.join(lst)
                    break
        left = partition+1; right = len(num)-1
        while left < right:
            lst = list(num)
            lst[left], lst[right] = lst[right], lst[left]
            num = ''.join(lst)
            #num[left], num[right] = num[right], num[left]
            left+=1; right-=1
        return num

    def permutation(self, s):
        perms = []
        t = s
        perms.append(s)
        s = self.nextPermutation(s)
        while s != t:
            perms.append(s)
            s = self.nextPermutation(s)
        return perms