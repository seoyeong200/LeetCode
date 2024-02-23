#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        find the start point number that appear in decreasing order        
        """
        n = len(nums)
        start_point = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                start_point = i
                break

        if start_point == n-2:
            nums[n-2], nums[n-1] = nums[n-1], nums[n-2]
            return
        elif start_point == -1:
            nums.sort()
            return
        
        min_val = 101
        for i in range(start_point, n):
            if nums[start_point] < nums[i] and nums[i] < min_val:
                min_idx, min_val = i, nums[i]
        nums[start_point], nums[min_idx] = nums[min_idx], nums[start_point]

        nums[start_point+1:] = sorted(nums[start_point+1:])
        nums = nums[:start_point+1] + nums[start_point+1:]



        
Solution().nextPermutation([1,3,2]) #[2,1,3]
# find the start point number that appear in decreasing order        
# @lc code=end

"""

(1, 2, 3, 4, 5)
5, 4)
4, 3, 5
5, 3
5, 3, 4
4, 3
3, 2, 4, 5
"""