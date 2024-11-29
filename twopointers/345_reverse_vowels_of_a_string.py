class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['u', 'e', 'o', 'a', 'i',
                  'U', 'E', 'O', 'A', 'I']
        char_list = list(s)
        i, j = 0, len(char_list) - 1
        while i < j:
            if char_list[i] in vowels:
                if char_list[j] in vowels:
                    char_list[i], char_list[j] = char_list[j], char_list[i]
                    i += 1
                    j -= 1
                else:
                    j -= 1
            else:
                i += 1

        return "".join(char_list)
    
# Join function reduce 10 times runtime