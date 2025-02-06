class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        nums_len, sub_sum = len(nums), sum(nums[: k])
        max_sum = sub_sum
        for i in range(k, nums_len):
            sub_sum = sub_sum - nums[i - k] + nums[i]
            max_sum = max(sub_sum, max_sum)
        return max_sum / float(k)

# 71.25%
