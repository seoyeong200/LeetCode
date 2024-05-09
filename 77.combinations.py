#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start

"""
[ Description ]
- return all possible combinations of k chosen from the range [1, n]
- n, k = 4, 2 -> [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        return combinations([i for i in range(1, n+1)], k)
# @lc code=end

