import math


class Solution(object):
    # precompute = [0] * 1000

    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        # prefix-sum approach with python3 - 100 %
        # if self.precompute[0] != 1:
        #     tmp = 0
        #     for i in range(1, 1001):
        #         tmp += i
        #         self.precompute[i - 1] = tmp
        # res = int(math.sqrt(self.precompute[n - 1]))
        # return res if res**2 == self.precompute[n - 1] else -1

        # math approach
        total = n * (n + 1) // 2
        res = int(math.sqrt(total))
        return res if res**2 == total else -1
