class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        checked = []
        for i in nums1:
            for index, j in enumerate(nums2):
                if i == j:
                    res.append(i)
        return res
    
# can use intersection
# stupid question
# TODO: Finish the problem
