# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # This is not two pointers
        # 46.36%
        # checked = {}
        # i = head
        # if i:
        #     checked[i] = True
        #     while i.next:
        #         if i.next in checked:
        #             return True
        #         checked[i] = True
        #         i = i.next
        # return False

        # Fast & Slow pointers
        # 79.76%
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return True
