#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if sum([i for i in range(1, k+1)]) > n or \
            sum([i for i in range(10-k, 10)]) < n:
            return []
        
        result = []
        def backtrack(cur: list, pos: int, target: int):
            """
            :cur: current stack(traced path)
            :pos: index of current position, 1-9 value
            :target: remained target value
            """
            if len(cur) == k:
                if target==0: result.append(cur[:])
                return
            # if len(cur)
            
            for i in range(pos, 10):
                cur.append(i)
                backtrack(cur, i+1, target-i)
                cur.pop()
                

        backtrack([], 1, n)
        return result

Solution().combinationSum3(3, 9) 
# @lc code=end

