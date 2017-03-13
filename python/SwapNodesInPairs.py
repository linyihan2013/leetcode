# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        if not head.next: return head
        safeG = ListNode(-1)
        safeG.next = head
        post = safeG
        cur = head
        pre = head.next
        while pre:
            tmp = pre.next
            pre.next = cur
            cur.next = tmp
            post.next = pre
            post = cur
            if not post.next: break
            cur = post.next
            pre = cur.next
        head = safeG.next
        del safeG
        return head