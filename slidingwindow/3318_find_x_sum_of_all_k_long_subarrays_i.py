class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        res, nums_len, i = [], len(nums), 0
        while i <= (nums_len - k):
            distinct_nums = list(set(nums[i: i + k]))
            if len(distinct_nums) <= x:
                res.append(sum(nums[i: i + k]))
                i += 1
                continue
            num_counter = {}
            for num in distinct_nums:
                num_counter[num] = nums[i: i + k].count(num)
            selected = sorted(num_counter.items(), key=lambda item: (
                item[1], item[0]), reverse=True)[:x]
            res.append(sum(map(lambda pair: pair[0] * pair[1], selected)))
            i += 1
        return res

# 75.00%
