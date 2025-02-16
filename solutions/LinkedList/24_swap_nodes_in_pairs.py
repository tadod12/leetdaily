# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        l, r, nxt = head, head.next, head.next.next
        l.next, r.next = nxt, l
        head, prev = r, l
        while nxt and nxt.next:
            l, r, nxt = nxt, nxt.next, nxt.next.next
            prev.next, l.next, r.next = r, nxt, l
            prev = l
        return head

# 100%
