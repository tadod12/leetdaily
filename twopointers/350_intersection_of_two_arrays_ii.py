class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Beat 5.19% =))
        # res = []
        # checked = []
        # for i in nums1:
        #     for index, j in enumerate(nums2):
        #         if i == j and index not in checked:
        #             res.append(i)
        #             checked.append(index)
        #             break
        # return res
        
        # Dict - 17.23%
        dict = {}
        for num in nums1:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        res = []
        for num in nums2:
            if num in dict:
                if dict[num] > 0:
                    res.append(num)
                    dict[num] -= 1
        return res
