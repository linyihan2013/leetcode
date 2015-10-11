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
        bufferSet = set()
        targetSet = set()
        if head is None:
            return head
        tmp = head
        while tmp:
            if tmp.val not in bufferSet:
                bufferSet.add(tmp.val)
            else:
                targetSet.add(tmp.val)
            tmp = tmp.next

        tmp = head
        while head and head.val in targetSet:
            tmp = head = head.next
        if head:
            next = head.next
        else:
            return None
        while next:
            if next.val not in targetSet:
                tmp = tmp.next
                next = next.next
            else:
                next = tmp.next = next.next
        return head