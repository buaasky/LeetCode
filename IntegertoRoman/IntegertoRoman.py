class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        rd = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        n = 1000
        s = ""
        while True:
            if n == 0:
                break
            a,num = divmod(num,n)
            while a != 0:
                if a == 9:
                    s += rd[n] + rd[n*10]
                    a = 0
                elif a >= 5:
                    s += rd[n * 5]
                    a = a -5
                elif a == 4:
                    s += rd[n] + rd[n * 5]
                    a = 0
                else:
                    s += rd[n]
                    a -= 1
            n = n // 10
        return s
        


if __name__ == "__main__":
    s = Solution()
    num = 3999
    sr = s.intToRoman(num)
    print(sr)