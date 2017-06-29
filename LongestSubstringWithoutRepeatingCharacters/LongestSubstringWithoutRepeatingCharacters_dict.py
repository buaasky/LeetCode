# copy from leetcode
# use dict and index to record the next start of string s. do not need to get the subString of s 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic,start,maxlength ={},0,0
        for i,letter in enumerate(s):
            if letter in dic:
                maxlength = max(maxlength, i - start)
                start = max(dic[letter] + 1, start)
            dic[letter] = i
        return max(maxlength, len(s) - start )

teststr = "pwwkew"
s = Solution()
result = s.lengthOfLongestSubstring(teststr)
print(result)
