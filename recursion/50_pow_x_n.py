class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        tmp = {
            0: 1.00000,
        }
        def recursion(x, n):
            if n in tmp:
                return tmp[n]
            if n < 0:
                tmp[n] = 1 / recursion(x, -n)
                return tmp[n]
            elif n % 2 == 0:
                tmp[n] = recursion(x, n//2) * recursion(x, n//2)
                return tmp[n] 
            else:
                tmp[n] = x * recursion(x, n-1)
                return tmp[n]
        return recursion(x, n)

