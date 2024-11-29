# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA and headB:
            i, j = headA, headB
            while i is not j:
                i = i.next if i else headB
                j = j.next if j else headA 
            return i
        return None

""" A little hint
    A) 1 - 2 - 3 \
                  5 - 6
    B)         4 /
    To walk all A then B: 1,2,3,5,6,4,5,6
    To walk all B then A: 4,5,6,1,2,3,5,6
"""