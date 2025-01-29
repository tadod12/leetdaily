class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        res = 0
        sorted_g, sorted_s = sorted(g), sorted(s)
        len_s, i_s = len(s), 0
        for el_g in sorted_g:
            if i_s >= len_s:
                break
            while i_s < len_s:
                if sorted_s[i_s] >= el_g:
                    res += 1
                    i_s += 1
                    break
                i_s += 1
        return res
