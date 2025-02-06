class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # sliding window but time exceed
        # sorted_nums = sorted(nums)
        # nums_len = len(nums)
        # sub_len = len(nums)
        # while sub_len > 0:
        #     start = 0
        #     while start <= nums_len - sub_len:
        #         if sorted_nums[start + sub_len - 1] - sorted_nums[start] == 1:
        #             return sub_len
        #         start += 1
        #     sub_len -= 1
        # return 0

        # hash - beats 5.19%
        # res = 0
        # distinct_nums = sorted(list(set(nums)))
        # dict_freq = {}
        # for num in distinct_nums:
        #     dict_freq[num] = nums.count(num)
        # for num in distinct_nums:
        #     if (num + 1) in dict_freq:
        #         res = max(res, dict_freq[num] + dict_freq[num + 1])
        # return res

        # hash without distinct - 93.17%
        res = 0
        dict_freq = {}
        for num in nums:
            if num in dict_freq:
                dict_freq[num] += 1
            else:
                dict_freq[num] = 1
        for num in dict_freq:
            if num + 1 in dict_freq:
                res = max(res, dict_freq[num] + dict_freq[num + 1])
        return res
