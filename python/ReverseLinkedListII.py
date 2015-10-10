__author__ = 'yihan'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m <= 0 or n <= 0:
            return head
        tmp = head
        nums = []
        if m > n:
            m, n = n, m
        for i in range(m - 1):
            if tmp.next:
                tmp = tmp.next
        tmp1 = tmp
        for i in range(n - m + 1):
            if tmp1:
                nums.append(tmp1.val)
                if tmp1.next:
                    tmp1 = tmp1.next
        tmp1 = tmp
        nums = nums[::-1]
        for i in range(n - m + 1):
            if tmp1:
                tmp1.val = nums[i]
                if tmp1.next:
                    tmp1 = tmp1.next
        return head