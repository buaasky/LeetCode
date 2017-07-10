class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 0
        if x < 0:
            flag = 1
            x = -x
        numstr = str(x)
        numstr = numstr[::-1]
        result = int(numstr)
        if result > 2147483647: #最大整数
            return 0
        else:
            if flag == 1:
                result = -result
            return result

s = Solution()
num = -123
a = s.reverse(num)
print(a)