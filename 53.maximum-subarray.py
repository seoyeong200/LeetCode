#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from time import time
from functools import cache
from typing import List
"""
[ Description ]
find the subarray with the largest sum, return its sum
- subarray means it remain the exact sequence of sub array
- [-2,1,-3,4,-1,2,1,-5,4] -> [4,-1,2,1] is the subarray which its sum is maximum

[ Solution ]
#1. Recursion
- calculate all of the possible subarrays and return the maximum value

#2. Dynamic Programming
- in tabulation manner(iteration)
    - dp[1][i] : maximum sum of subarray ending at i
        - each index, update dp[1][i] as 
            MAX(Only choosing current element, Extending from previous subarray and choosing current element)
            = MAX(nums[i], dp[1][i-1]+nums[i])

    - dp[0][i] : maximum sum of subarray upto i
        - each index, update dp[0][i] as
            MAX(Maximize sum subarray found till last index, Maximize sum subarray found ending at current index)
            = MAX(dp[0][i-1], dp[1][i])


#3. Divide and Conquer
- recursion, left&right, calculate mid index value and compare the size of left / right subarray's maximized sum
    - return the maximum value of 
    DC_Function(l, mid-1), 
    DC_Function(mid+1, r), 
    l_sum+nums[mid]+r_sum
        - l_sum : sub-sum max of l ~ mid-1
        - r_sum : sub-sum max of mid+1 ~ r


"""
class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        return self.maxSubArray_tabulationDP(nums)

    def maxSubArray_recursive(self, nums: List[int]) -> int:
        def subarray(i, must_pick):
            if i >= len(nums): return 0 if must_pick else -inf
            # T_returnVal = subarray(i+1, True)
            # F_returnVal = subarray(i+1, Fals e)
            # return max(nums[i]+T_returnVal, 0 if must_pick else F_returnVal)
            return max(nums[i]+subarray(i+1, True), 0 if must_pick else subarray(i+1, False))
        
        @cache
        def subarray_cache(i, must_pick):
            if i >= len(nums): return 0 if must_pick else -inf
            return max(nums[i]+subarray_cache(i+1, True) , 0 if must_pick else subarray_cache(i+1, False))

        inf = 1e10
        start = time(); ans = subarray(0, False); end = time()
        print(f"time without caching : {end-start}")

        start = time(); ans = subarray_cache(0, False); end = time()
        print(f"time with caching : {end-start}")

        print(ans)

    def maxSubArray_tabulationDP(self, nums: List[int]) -> int:
        
        def plain():
            dp =[[0 for _ in range(n)] for _ in range(2)]
            dp[0][0], dp[1][0] = nums[0], nums[0]
            for i in range(1, n):
                dp[1][i] = max(nums[i], dp[1][i-1]+nums[i])
                dp[0][i] = max(dp[0][i-1], dp[1][i])
            return dp[0][-1]
        
        def optimize():
            dp = [0 for _ in range(n)]
            dp[0] = nums[0]
            for i in range(1, n):
                dp[i] = max(nums[i], dp[i-1]+nums[i])
            return max(dp)
        
        n = len(nums)
        return optimize()
    
    def maxSubArray_divide_conquer(self, nums: List[int]) -> int: 
        def maximized_subarray(l: int, r: int, i: int) -> int:
            if l>r: return -inf
            mid = (l+r)//2
            l_sum, tmp = 0, 0
            for idx in range(mid-1, l-1, -1): l_sum = max(l_sum, tmp:=tmp+nums[idx])

            r_sum, tmp = 0, 0
            for idx in range(mid+1, r+1): r_sum = max(r_sum, tmp:=tmp+nums[idx])

            left_max = maximized_subarray(l, mid-1, i+1)
            right_max = maximized_subarray(mid+1, r, i+1)
            return max(left_max, right_max, l_sum+nums[mid]+r_sum)
        
        inf = 1e10
        maximized_subarray(0, len(nums)-1, 0)
        
        
# @lc code=end
Solution().maxSubArray_divide_conquer([-2,1,-3,4,-1,2,1,-5,4])
# Solution().maxSubArray_recursive([-2,1])

"""
0SA(0, 8) -> l_sum=4, r_sum=3
0calculate left maximized subarray = 4
    1_SA(0, 3) -> l_sum=0, r_sum=1
    1_calculate left maximized subarray = -2
        2__SA(0, 0) -> l_sum=0, r_sum=0
        2__calculate left maximized subarray = -inf
            3___return -inf
        2__calculate right maximized subarray = -inf
            3___return -inf
        2__return max(-10000000000.0, -10000000000.0, -2)

    1_calculate right maximized subarray = 4
        2__SA(2, 3) -> l_sum=0, r_sum=4
        2__calculate left maximized subarray
            3___return -inf
        2__calculate right maximized subarray
            3___SA(3, 3) -> l_sum=0, r_sum=0
            3___calculate left maximized subarray
                4____return -inf
            3___calculate right maximized subarray = -inf
                4____return -inf
            3___return max(-10000000000.0, -10000000000.0, 4)
        2__return max(-10000000000.0, 4, 1)

    1_return max(-2, 4, 2)


0calculate right maximized subarray
    1_SA(5, 8) -> l_sum=2, r_sum=0
    1_calculate left maximized subarray
        2__SA(5, 5) -> l_sum=0, r_sum=0
        2__calculate left maximized subarray
            3___return -inf
        2__calculate right maximized subarray
            3___return -inf
        2__return max(-10000000000.0, -10000000000.0, 2)

    1_calculate right maximized subarray
        2__SA(7, 8) -> l_sum=0, r_sum=4
        2__calculate left maximized subarray
            3___return -inf
        2__calculate right maximized subarray
            3___SA(8, 8) -> l_sum=0, r_sum=0
            3___calculate left maximized subarray
                4____return -inf
            3___calculate right maximized subarray
                4____return -inf
            3___return max(-10000000000.0, -10000000000.0, 4)
        2__return max(-10000000000.0, 4, -1)

    1_return max(2, 4, 3)

0return max(4, 4, 6)

"""