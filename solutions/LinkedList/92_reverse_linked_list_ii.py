# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if left == right or not head or not head.next:
            return head

        l_out, l_in, r_in, r_out = head, None, None, None
        tmp = head
        for i in range(1, right):
            if i == left - 1:
                l_out = tmp
            elif i == left:
                l_in = tmp
            tmp = tmp.next
        r_in, r_out = tmp, tmp.next

        # reversing
        prev = l_in
        curr = l_in.next
        while curr != r_in:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        curr.next = prev

        # finishing
        if l_out != l_in:
            l_out.next = curr
        l_in.next = r_out

        if l_out == l_in:
            return r_in
        return head
