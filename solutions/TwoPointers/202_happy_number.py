# Stupid number actually
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def calculate(n):
            res = 0
            while n != 0:
                res += (n % 10)**2
                n //= 10
            return res

        # ridiculous solution
        # for i in range(0, 10):
        #     n = calculate(n)
        #     if n == 1:
        #         return True
        # return False

        # fast & slow pointers
        slow = calculate(n)
        fast = calculate(calculate(n))
        while slow != fast:
            slow = calculate(slow)
            fast = calculate(calculate(fast))
        return slow == 1
        # 71.80%
