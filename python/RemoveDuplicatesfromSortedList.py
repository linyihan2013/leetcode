__author__ = 'yihan'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dupSet = set()
        if head is None:
            return head
        dupSet.add(head.val)
        tmp = head
        next = head.next
        while next:
            if next.val not in dupSet:
                dupSet.add(next.val)
                tmp = tmp.next
                next = next.next
            else:
                next = tmp.next = next.next
        return head