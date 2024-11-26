class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def valid_char(c):
            if '0' <= c <= '9' \
                or 'a' <= c <= 'z' \
                or 'A' <= c <= 'Z':
                return True
            return False

        i, j = 0, len(s) - 1
        while i < j:
            if valid_char(s[i]):
                while (not valid_char(s[j])) and i < j:
                    j -= 1
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False
            else:
                i += 1
        return True