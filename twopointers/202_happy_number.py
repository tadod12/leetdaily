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
        for i in range(0, 10):
            n = calculate(n)
            if n == 1:
                return True
        return False
        
# Beats 74.08%
