# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # Fast & Slow pointers - 75.00%
        if not head or not head.next:
            return head

        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # Reverse right half
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # Reorder
        left, right = head, prev
        while right:
            tmp_l, tmp_r = left.next, right.next
            left.next = right
            right.next = tmp_l
            left, right = tmp_l, tmp_r
