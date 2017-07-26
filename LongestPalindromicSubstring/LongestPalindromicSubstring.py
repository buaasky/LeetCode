# Manacher算法 (代码待优化！！！！)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        p = 0
        p0 = 0
        new_s = ""
        for i in s:
            new_s += i + "#"
        new_s = "$" + new_s[:-1] + "$"
        l = [1] * len(new_s)
        for i,word in enumerate(new_s):
            if i == 0:
                continue
            if i > p:
                count = 1
                while i+count< len(new_s) and new_s[i-count] == new_s[i+count]:
                    count += 1
                l[i] = count
                if i + count - 1 > p:
                    p = i + count - 1
                    p0 = i
            else:
                j = 2 * p0 - i
                if j >= 0 and  l[j] < p - i:
                    l[i] = l[j]
                else:
                    count = p - i
                    while i - count >=0 and i + count < len(new_s)  and new_s[i - count] == new_s[i + count]:
                        count += 1
                    l[i] = count
                    if i + count - 1 > p:
                        p = i + count - 1
                        p0 = i
        result = ""
        for i,j in enumerate(l):
            tempresult = new_s[i-j + 1:i+j].replace("#","").replace("$","")
            if len(tempresult) > len(result):
                result = tempresult
        return result
                
        
if __name__ == "__main__":
    s = Solution()
    sr = "abb"
    a = s.longestPalindrome(sr)
    print(a)
    
