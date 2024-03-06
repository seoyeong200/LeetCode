#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
"""
[ Description ]
- numbers is non-decreasing sorted 1-array
- return the indices of two numbers such that they add up to target
eg.
- numbers = [2,7,11,15], target = 9 -> [1, 2]
- numbers = [2,3,4], target = 6 -> [1, 3]
- numbers = [-1,0], target = -1 -> [1, 2]

"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l<r:
            s = numbers[l] + numbers[r]
            if s == target: return [l+1, r+1]
            elif s > target: r-=1
            else: l+=1
# @lc code=end

