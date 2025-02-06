class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 1:
            return 0 if nums[0] == val else 1

        i, j = 0, len(nums)
        for i in range(0, j):
            if nums[i] == val:
                for j in range(j - 1, i - 1, -1):
                    if nums[j] != val:
                        nums[i] = nums[j]
                        nums[j] = val
                        break
        return j

# Beats 100.00%
