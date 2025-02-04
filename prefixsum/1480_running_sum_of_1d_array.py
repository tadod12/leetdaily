class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 20.19%
        # tmp, nums_len = 0, len(nums)
        # for i in range(0, nums_len):
        #     tmp += nums[i]
        #     nums[i] = tmp
        # return nums

        # 100%
        nums_len = len(nums)
        for i in range(1, nums_len):
            nums[i] = nums[i] + nums[i - 1]
        return nums
