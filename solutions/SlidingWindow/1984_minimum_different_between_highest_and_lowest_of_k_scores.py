class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        sorted_nums = sorted(nums)
        res, i, nums_len = 9223372036854775807, 0, len(nums)
        while i <= nums_len - k:
            res = min(res, sorted_nums[i + k - 1] - sorted_nums[i])
            i += 1
        return res

# 90.67%
