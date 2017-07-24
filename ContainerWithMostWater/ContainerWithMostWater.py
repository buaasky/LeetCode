#暴力搜索
# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         maxArea = 0
#         pre = 0
#         if height == []:
#             return maxArea
#         for i in range(len(height)):
#             if i == len(height) - 1:
#                 break
#             pre = height[i]
#             for j in range(i+1,len(height)):
#                 m = min(height[i],height[j])
#                 tempArea = m * (j - i)
#                 maxArea = max(maxArea,tempArea)
#         return maxArea

# discuss中的代码思路
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        left = 0
        right = len(height) - 1
        while left < right:
            maxArea = max(maxArea,min(height[left],height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea



if __name__ == "__main__":
    s = Solution()
    height = [2,1]
    area = s.maxArea(height)
    print(area)