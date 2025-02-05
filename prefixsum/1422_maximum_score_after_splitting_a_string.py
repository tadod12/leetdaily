class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, tmp, s_len = 0, s.count('1'), len(s)
        for i in range(0, s_len - 1):
            if s[i] == '1':
                tmp -= 1
            else:
                tmp += 1
            res = max(res, tmp)
        return res
