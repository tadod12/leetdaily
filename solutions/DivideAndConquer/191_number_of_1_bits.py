# beat 100%
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        else:
            res = n%2 + self.hammingWeight(n//2)
        return res
        