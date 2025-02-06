class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len, nums_sum = len(nums), sum(nums)
        if nums_sum % 2 == 0:
            # don't need prefix-sum for this shit
            return nums_len - 1
        return 0

# of course 100.00%
