class Solution(object):
    string = "a"

    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        if k <= len(self.string):
            return self.string[k-1]
        else:
            append = ""
            for char in self.string:
                if chr != "z":
                    append += chr(ord(char) + 1)
                else:
                    append += "a"
            self.string += append
            return self.kthCharacter(k)
