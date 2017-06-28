class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numdict = {}
        for index,item in enumerate(nums):
            if item in numdict:
                return [numdict[item],index]
            else:
                numdict[target - item] = index

s = Solution()
mylist = [2, 7, 11, 15]
target = 9
a = s.twoSum(mylist,target)
print(a)
        