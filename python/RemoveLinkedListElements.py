__author__ = 'yihan'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        while head and head.val is val:
            head = head.next
        tmp = head
        while tmp and tmp.next:
            while tmp.next and tmp.next.val is val:
                tmp.next = tmp.next.next
            tmp = tmp.next
        return head