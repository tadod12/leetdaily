class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 34.25%
        # res, nums_len, win_size = 0, len(nums), 1
        # while win_size <= len(nums):
        #     i = 0
        #     while i <= nums_len - win_size:
        #         if abs(nums[i] - nums[i + win_size - 1]) <= min(nums[i], nums[i + win_size - 1]):
        #             res = max(res, nums[i] ^ nums[i + win_size - 1])
        #         i += 1
        #     win_size += 1
        # return res

        # sort first - 82.19%
        res, sorted_nums = 0, sorted(nums)
        for i, m in enumerate(sorted_nums):
            for n in sorted_nums[i:]:
                if n - m <= m:
                    res = max(res, n ^ m)
        return res
