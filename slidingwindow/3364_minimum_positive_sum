class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        
        # 26.49% - stupid by not using sliding window
        # res = -1
        # nums_len, i = len(nums), 0
        # while i <= nums_len - l:
        #     for j in range(l, r + 1):
        #         tmp = sum(nums[i:i+j])
        #         if tmp > 0:
        #             res = min(res, tmp) if res > 0 else tmp
        #     i += 1
        # return res

        # sliding window with each size
        nums_len, res = len(nums), -1
        for sub_len in range(l, r + 1):
            sub_sum, head_sub = sum(nums[0 : sub_len]), 0
            if sub_sum > 0:
                res = min(res, sub_sum) if res > 0 else sub_sum
            for i in range(sub_len, nums_len):
                sub_sum, head_sub = sub_sum + nums[i] - nums[head_sub], head_sub + 1
                if sub_sum > 0:
                    res = min(res, sub_sum) if res > 0 else sub_sum
        return res
