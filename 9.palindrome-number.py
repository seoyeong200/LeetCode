#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
"""
거꾸로 뒤집어도 동일한 문자열, 즉 palindrome인지 판별하는 시스템
"""
# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        solve it with O(n) algorithm
        """
        # when the input is less than 0, always not palindrome so
        # return false when x<0
        if x<0: return False
        x = str(x)
        n = len(x)
        for i in range(n):
            reverse_i = n-1-i
            if x[i] != x[reverse_i]: return False
        return True

# @lc code=end
inp = -121  
inp = 10
ans = Solution().isPalindrome(inp)
print(ans)

