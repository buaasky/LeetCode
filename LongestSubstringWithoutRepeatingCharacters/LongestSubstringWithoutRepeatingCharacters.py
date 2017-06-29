class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlength = 0
        substr = "";
        for letter in s:
            if letter not in substr:
                substr += letter
            else:
                maxlength = max(maxlength,len(substr))
                substr += letter
                substr = substr[substr.index(letter)+ 1:]
        return max(maxlength,len(substr))
    
teststr = "pwwkew"
s = Solution()
result = s.lengthOfLongestSubstring(teststr)
print(result)
