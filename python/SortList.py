__author__ = 'yihan'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        else:
            fast = slow = head
            while fast.next is not None and fast.next.next is not None:
                fast = fast.next.next
                slow = slow.next
            fast = slow
            slow = slow.next
            fast.next = None
            fast = self.sortList(head)
            slow = self.sortList(slow)
            return self.merge(fast, slow)

    def merge(self, head1, head2):
        if head1 is None: return head2
        if head2 is None: return head1
        res, p = None, None
        if head1.val < head2.val:
            res = head1
            head1 = head1.next
        else:
            res = head2
            head2 = head2.next
        p = res
        while head1 and head2:
            if head1.val < head2.val:
                p.next = head1
                head1 = head1.next
            else:
                p.next = head2
                head2 = head2.next
            p = p.next
        if head1: p.next = head1
        else: p.next = head2
        return res