class Solution(object):
    tmp = []

    def test(self, nums, res):
        for num in nums:
            if num not in self.tmp:
                self.tmp.append(num)
                if len(self.tmp) == len(nums):
                    tmp = self.tmp[:]
                    res.append(tmp)
                else:
                    self.test(nums, res)
                self.tmp.pop()

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.test(nums, res)
        return res
