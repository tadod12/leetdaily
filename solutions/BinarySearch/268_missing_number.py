class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # This approach not good enough - Beat 30.75%
        # sorted_nums = sorted(nums)
        # i = 0
        # for num in sorted_nums:
        #     if num == i:
        #         i += 1
        #     else:
        #         return i

        # Hash solution - Beat 60.52%
        # arr = [0] * len(nums)
        # for num in nums:
        #     arr[num] = 1
        # for i, a in enumerate(arr):
        #     if a == 0:
        #         return i
            
        # The sum solution - Beat 67.09%
        nums_len = len(nums)
        expected_sum = (nums_len * (nums_len + 1)) / 2
        actual_sum = 0
        for num in nums:
            actual_sum += num
        return expected_sum - actual_sum
   