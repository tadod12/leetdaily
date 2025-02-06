class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rl, lr, nums_len = nums[:], nums[:], len(nums)
        for i in range(1, nums_len):
            rl[i] = rl[i] + rl[i - 1]
            lr[-i-1] = lr[-i-1] + lr[-i]
        for i in range(0, nums_len):
            if rl[i] == lr[i]:
                return i
        return -1
