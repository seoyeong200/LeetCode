#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        memory 효율(beats 98.84%)은 좋지만 시간 효율(beats 9.38%)은 떨어지는 풀이
        """
        left, right = 0, len(height)-1
        max_area = 0
        print(left, right, max_area)
        while left <= right:
            current_area = min(height[left], height[right]) * (right-left)
            max_area = max(max_area, current_area)
            print(left, right, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


    def maxArea_timeout(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        for i in range(n):
            for j in range(i+1, n):
                ans = max(ans, (j-i) * min(height[i], height[j]))
        return ans




        
Solution().maxArea([1,8,6,2,5,4,8,3,7])
