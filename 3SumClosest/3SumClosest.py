import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        t = 0
        gap = sys.maxsize
        for i in range(len(nums)-2):
            if i == 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while r > l:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return target
                elif s > target:
                    if gap > s - target:
                        gap = s - target
                        t = s
                    while r > l and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
                else:
                    if gap > target - s:
                        gap = target - s
                        t = s
                    while r > l and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
        return t
            
                


                

if __name__ == "__main__":
    s = Solution()
    nums = [1,6,9,14,16,70]
    target = 81
    r = s.threeSumClosest(nums,target)
    print(r)