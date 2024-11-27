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
        checked = {}
        i = head
        if i:
            checked[i] = True
            while i.next:
                if i.next in checked:
                    return True
                checked[i] = True
                i = i.next
        return False
    
# This is not two pointers
# 46.36%
