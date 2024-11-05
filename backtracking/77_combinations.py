class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def backtracking(start, tmp):
            for i in range(start, n+1):
                tmp.append(i)
                if len(tmp) == k:
                    a = tmp[:]
                    res.append(a)
                else:
                    backtracking(i + 1, tmp)
                tmp.pop()
        backtracking(start=1, tmp=[])
        return res