class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # prefix-sum - 41.51%
        # lr, rl, nums_len = nums[:], nums[:], len(nums)
        # lr[0], rl[-1] = 0, 0
        # for i in range(1, nums_len):
        #     lr[i] = lr[i - 1] + nums[i - 1]
        #     rl[-i - 1] = rl[-i] + nums[-i]
        # nums[0], nums[-1] = rl[0], lr[-1]
        # for i in range(1, nums_len - 1):
        #     nums[i] = abs(lr[i] - rl[i])
        # return nums

        # suffix
        res, suffix_sum, prefix_sum = [], sum(nums), 0
        for num in nums:
            prefix_sum += num
            res.append(abs(suffix_sum - prefix_sum))
            suffix_sum -= num
        return res
