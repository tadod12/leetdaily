# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # Two pointers style - 44.49%
        # nums_list = []
        # curr = head
        # if curr:
        #     while curr.next:
        #         nums_list.append(curr.val)
        #         curr = curr.next
        #     i, j = 0, len(nums_list) - 1
        #     while i < j:
        #         if nums_list[i] != nums_list[j]:
        #             return False
        #         i += 1
        #         j -= 1
        #     return True
        # else:
        #     return True

        # Recursion style - TOO MANY SWEAT
        # res = [False]
        # def recursion(curr_node, stack, flag):
        #     if curr_node:
        #         if flag == False:
        #             if curr_node.val == stack[-1]:
        #                 tmp1 = stack[-1]
        #                 recursion(curr_node.next, tmp1, True)

        #             if len(stack) >= 2 and curr_node.val == stack[-2]:
        #                 tmp2 = stack[:-2]
        #                 recursion(curr_node.next, tmp2, True)

        #             stack.append(curr_node.val)
        #             recursion(curr_node.next, stack, flag)
        #         else:
        #             if curr_node.val != stack[-1]:
        #                 return
        #             else:
        #                 stack.pop()
        #     else:
        #         if flag == False and len(stack) == 1:
        #             res.append(True)
        #         elif len(stack) == 0:
        #             res.append(True)

        # recursion(head.next, [head.val], False)
        # return res[-1]

        # Fast & Slow pointers - best
        # 93.89%
        slow, fast = head, head
        left_half = []
        while fast and fast.next:
            left_half.append(slow.val)
            slow, fast = slow.next, fast.next.next
        slow = slow if fast is None else slow.next
        while slow:
            if left_half[-1] != slow.val:
                return False
            left_half.pop()
            slow = slow.next
        return True
