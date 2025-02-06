class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Simulation - Time Limit Exceeded
        # res, nums_len = 0, len(nums)
        # for i, num in enumerate(nums):
        #     if num == 0:
        #         for j in [-1, 1]:
        #             tmp_nums = nums[:]
        #             d = j  # direction
        #             k = i + d  # next pos
        #             while k in range(0, nums_len):
        #                 if tmp_nums[k] == 0:
        #                     k += d
        #                 else:
        #                     tmp_nums[k] -= 1
        #                     d *= -1
        #                     k += d
        #             if sum(tmp_nums) == 0:
        #                 res += 1
        # return res

        # Tricky way
        res, nums_len, sum_nums = 0, len(nums), nums[:]
        for i in range(1, nums_len):
            sum_nums[i] += sum_nums[i - 1]
        for i, num in enumerate(nums):
            if num == 0:
                left = sum_nums[i]
                right = sum_nums[nums_len - 1] - left
                if left == right:
                    res += 2
                elif left - right in [-1, 1]:
                    res += 1
        return res
