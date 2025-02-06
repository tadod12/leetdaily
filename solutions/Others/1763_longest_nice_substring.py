class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return ""
        
        characters_list = set(s) # get all diff chars

        for i, c in enumerate(s):
            if c.swapcase() not in characters_list:
                left_len = self.longestNiceSubstring(s[0:i]) # index 0 to i-1
                right_len = self.longestNiceSubstring(s[i+1:len(s)+1]) # index i+1 to end

                return left_len if len(left_len) >= len(right_len) else right_len
            
        return s
        


"""Solution - Find the invalid character
E.g. if we are given "YazaAay"

Then if we see, all the characters have their lowercase and uppercase variants except only "z".
This means that we can never have a valid subarray with "z" in it. 

So, we need to look for a valid subarray before "z" and after "z" only. In this string there is 
only one invalid character but there can be multiple. So, we simply create a set of all the 
characters and then, while looping over the string, just check if that character has its case 
variation in the set or not. If not, that means it is an invalid character and we need to find 
the valid substring before and after this character's index. 

So we will make two recursive calls. One for finding a valid substring from beginning to the 
invalid character's index (excluding it) and the other to find a valid substring from the invalid 
character's index + 1 to the end of the string. And if we get a valid substring out of both or 
even from just one, that means, just return the one that's longer.

It is also possible that a string is already nice. e.g. "aAa". In this case, the recursive calls 
won't be made since they are only made when we encounter an invalid character. So in such cases, 
we can return the string itself at the end.
"""