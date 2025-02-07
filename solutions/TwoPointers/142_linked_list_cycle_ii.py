# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Cycle check
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                # Find the cycle's length
                cycle_len, tmp = 1, slow.next
                while tmp != slow:
                    tmp = tmp.next
                    cycle_len += 1

                # Find the start point
                slow, fast = head, head
                while cycle_len > 0:
                    fast = fast.next
                    cycle_len -= 1
                while fast != slow:
                    slow, fast = slow.next, fast.next

                return slow
        return None

# 42.74%
