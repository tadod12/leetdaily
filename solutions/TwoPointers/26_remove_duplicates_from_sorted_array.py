class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, 1
        while j < len(nums):
            if nums[j] == nums[i]:
                j += 1
            else:
                nums[i + 1] = nums[j]
                i += 1
        return i + 1

# 100.00%
# https://leetcode.com/problem-list/two-pointers/?difficulty=EASY
