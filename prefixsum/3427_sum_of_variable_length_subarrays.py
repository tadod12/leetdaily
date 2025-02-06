class Solution(object):
    def subarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, nums_len = nums[0], len(nums)
        for i in range(1, nums_len):
            sub = i - nums[i]
            nums[i] += nums[i - 1]
            res += nums[i] if sub <= 0 else nums[i] - nums[sub - 1]
        return res
