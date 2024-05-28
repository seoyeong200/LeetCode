#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        # global answer 
        answer = 1e10

        def backtrack(idx: int, sum: int, cnt: int):
            global answer
            
            if cnt == 3:
                answer = sum if abs(target-sum) < abs(target-answer) else answer
                return
            if idx >= len(nums): return
            
            backtrack(idx+1, sum+nums[idx], cnt+1)
            backtrack(idx+1, sum, cnt)
        backtrack(0, 0, 0)
        return answer
        


    def threeSumClosest_timeexceed(self, nums: List[int], target: int) -> int:
        from itertools import combinations

        candidate = list(combinations([i for i in range(len(nums))], 3))
        answer = 1e10
        for i, j, k in candidate:
            present_sum = nums[i]+nums[j]+nums[k]
            if abs(target-present_sum) < abs(target-answer): answer = present_sum

        return answer
# @lc code=end

