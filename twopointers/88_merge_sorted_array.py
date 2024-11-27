class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        if n == 0:
            return 

        while j < n and i < len(nums1):
            if (i >= m + j and nums1[i] == 0) or (nums1[i] >= nums2[j]):
                nums1.insert(i, nums2[j])
                nums1.pop()
                i += 1
                j += 1
            else:
                i += 1

# 100.00%, nice troll at the remain 0
