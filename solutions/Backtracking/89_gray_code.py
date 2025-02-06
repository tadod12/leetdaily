class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Time exceed
        # res = [0]
        # def cal(tmp):
        #     res = 0
        #     p = 1
        #     for i in reversed(tmp):
        #         res += i * p
        #         p *= 2
        #     return res
        # def backtracking(tmp):
        #     a = tmp[:]
        #     for i in range(n - 1, -1, -1):
        #         a[i] = 1 - a[i]
        #         b = cal(a)
        #         if b not in res:
        #             res.append(b)
        #             backtracking(a)
        #         a[i] = 1 - a[i]
        # backtracking([0]*n)
        # return res

        res = []
        for i in range(0,1<<n):
            res.append(i^(i>>1))
        return res