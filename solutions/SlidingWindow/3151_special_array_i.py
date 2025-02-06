class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i, nums_len = 0, len(nums)
        if nums_len <= 1:
            return True
        while i < nums_len - 1:
            if (nums[i] + nums[i + 1]) % 2 == 0:
                return False
            i += 1
        return True

# 100.00%
