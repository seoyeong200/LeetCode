#
# @lc app=leetcode id=2149 lang=python3
#
# [2149] Rearrange Array Elements by Sign
#

# @lc code=start
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive, negative = [], []
        for n in nums:
            if n > 0: positive.append(n)
            else: negative.append(n)
        ans = []
        for p, n in zip(positive, negative):
            ans.append(p)
            ans.append(n)
        return ans

        
# @lc code=end

