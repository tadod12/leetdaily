class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        # 65.24% - no need 3 for loops
        # dict, monotonic_stack, res, len_nums2 = {}, [], [], len(nums2)
        # for num in nums2:
        #     dict[num] = -1
        # for i in range(0, len_nums2):
        #     while monotonic_stack and nums2[i] > monotonic_stack[-1]:
        #         num = monotonic_stack.pop()
        #         dict[num] = nums2[i]
        #     monotonic_stack.append(nums2[i])
        # for num in nums1:
        #     res.append(dict[num])

        # return res
    
        # 100%
        dict, monotonic_stack = {}, []
        for num in nums2:
            while monotonic_stack and num > monotonic_stack[-1]:
                dict[monotonic_stack.pop()] = num
            monotonic_stack.append(num)
        # less iterations
        while monotonic_stack:
            dict[monotonic_stack.pop()] = -1
        return [dict[num] for num in nums1]
    