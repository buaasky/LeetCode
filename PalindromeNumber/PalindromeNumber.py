class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        range = 1
        while range <= x//10:
            range *= 10
        while x > 0:
            left = x%10
            right = x // range
            if left != right:
                return False
            x = x - right * range  - left
            range = range // 100
            x = x // 10
        return True

s = Solution()
x = 11
a = s.isPalindrome(x)
print(a)