# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if strs == []:
#             return ""
#         prefix = strs[0]
#         tempprefix = prefix
#         for i in zip(*strs):
#             print(i)
#         for i in strs[1:]:
#             m = min(len(prefix),len(i))
#             tempprefix = ""
#             for j in range(m):
#                 if prefix[j] == i[j]:
#                     tempprefix += prefix[j]
#                 else:
#                     break
#             if len(tempprefix) < len(prefix):
#                 prefix = tempprefix
#         return tempprefix

# using zip and set
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        prefix = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                prefix += i[0]
            else:
                break
        return prefix

if __name__ == "__main__":
    s = Solution()
    strs = ["acas","acad","acda"]
    print(s.longestCommonPrefix(strs))