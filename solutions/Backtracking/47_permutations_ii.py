class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []  # final result
        lenght = len(nums)
        def backtracking(index, tmp, indexed):
            for i in range(0, lenght):
                if not indexed[i]:
                    tmp.append(nums[i])
                    indexed[i] = True
                    if index == lenght and tmp not in res:
                        a = tmp[:]
                        res.append(a)
                    else:
                        backtracking(index + 1, tmp, indexed)
                    tmp.pop()
                    indexed[i] = False

        backtracking(index=1, tmp=[], indexed=[False]*lenght)
        return res

