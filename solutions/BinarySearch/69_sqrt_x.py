class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        l, r = 1, x
        while l < r:
            m = (l + r) // 2
            if m * m == x:
                return m
            elif m * m > x:
                r = m - 1
            else:
                l = m + 1
        if l * l > x:
            return l
        else:
            return l + 1
        
# Beats 100.00%
        