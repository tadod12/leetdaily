class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        def backtracking(tmp):
            for num in nums:
                if len(tmp) == 0 or (num not in tmp and num > tmp[-1]):
                    tmp.append(num)
                    if tmp not in res:
                        a = tmp[:]
                        res.append(a)
                    backtracking(tmp)
                    tmp.pop()
        backtracking([])
        return res