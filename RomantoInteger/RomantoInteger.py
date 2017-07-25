# class Solution(object):
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         # rd = {"I":1, "V":5, "X":10,"L":50, "C":100, "D":500, "M":1000}
#         n = 0
#         strs = ['CM',"M",  'CD','D', 'XC', 'C', 'XL', 'L', 'IX',  'X','IV', 'V',  'I']
#         nums = [ 900,1000, 400, 500,  90,100,  40,50, 9, 10,  4, 5, 1]
#         for i,j in enumerate(strs):
#             while j in s:
#                 n += nums[i]
#                 s = s.replace(j,"",1)
#         return n

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rd = {"I":1, "V":5, "X":10,"L":50, "C":100, "D":500, "M":1000}
        n = 0
        for i in range(len(s)-1):
            if rd[s[i]] < rd[s[i+1]]:
                n -= rd[s[i]]
            else:
                n += rd[s[i]]
        n += rd[s[-1]]
        return n

if __name__ == "__main__":
    s = Solution()
    sr = "IV"
    num = s.romanToInt(sr)
    print(num)