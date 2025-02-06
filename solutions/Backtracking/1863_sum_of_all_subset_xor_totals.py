class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [0]
        nums_len = len(nums)
        checked = [False] * nums_len
        tmp = []

        def xor(list):
            return reduce(lambda i, j: i ^ j, list)

        def backtracking(index, prev_i):
            for i in range(prev_i + 1, nums_len):
                if not checked[i]:
                    tmp.append(nums[i])
                    checked[i] = True
                    res.append(xor(tmp))
                    print(tmp)
                    if i < nums_len-1:
                        backtracking(index + 1, i)
                    tmp.pop()
                    checked[i] = False

        backtracking(0, -1)
        return sum(res)