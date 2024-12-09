class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        l, r = 0, num
        while l <= r:
            m = (l + r) // 2
            if m * m == num:
                return True
            elif m * m > num:
                r = m - 1
            else:
                l = m + 1
        
        return False
    
# Beats 100.00%
