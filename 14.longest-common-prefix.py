#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start


from typing import List

"""
f l o w e r
f l o w
f l i g h t

a=["Johnny", "Mike", "Dave"]
x=zip(*a)
print(tuple(x))
(('J', 'D', 'M'), ('o', 'a', 'i'), ('h', 'v', 'k'), ('n', 'e', 'e'))
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        for each_s in zip(*strs):
            if len(set(each_s)) == 1:
                ans += each_s[0]
            else:
                return ans
        return ans


    def longestCommonPrefix_initial(self, strs: List[str]) -> str:
        n = len(strs)
        ans = ''
        min_l = 1e10
        for i in range(n):
            min_l = min(min_l, len(strs[i]))

        idx = 0
        while idx < min_l:
            tmp = strs[0][idx]
            for str in strs[1:]:
                if tmp != str[idx]: return ans
            ans += tmp
            idx+=1
        return ans

# @lc code=end

