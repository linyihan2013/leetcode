# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        p, q = head, head
        while q:
            q = q.next
            if not q or not q.next: break
            next_p, next_q = p.next, q.next
            q.next = next_q.next
            p.next, next_q.next = next_q, next_p
            p = p.next
        return head