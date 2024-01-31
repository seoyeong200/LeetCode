#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
"""
1/2개씩 계단을 올라갈 수 있을 때, n개를 오르는 모든 경우의 수?
"""

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        dp[i] = i개의 계단을 오르는 모든 경우의 수의 개수
        """
        dp = [0 for _ in range(n+1)]
        if n in [1, 2]: return n
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1]+ dp[i-2]

        return dp[n]

# @lc code=end

