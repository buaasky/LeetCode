class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if len(digits) == 1:
            # tempstr = dic[digits]
            l = [i for i in dic[digits]]
            return l
        else:
            # tempstr = dic[digits[0]]
            # l = []
            # for i in tempstr:
            #     templ = self.letterCombinations(digits[1:])
            #     templ = [i + j for j in templ]
            #     l = l + templ
            templ = self.letterCombinations(digits[1:])
            l = [i + j for i in dic[digits[0]] for j in templ]
            return l
        

            
# 使用列表解析可以简化代码，提高运行速度
if __name__ == "__main__":
    s = Solution()
    digits = "23"
    l = s.letterCombinations(digits)
    for i in l:
        print(i)