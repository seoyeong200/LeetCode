#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        """
        reverse givin integer, and return 0 when the result intger exceed 32 bits
        bin() complexity : O(log(n))
        """
        str_X = str(abs(x))
        reverse_x = int(''.join([x for x in str_X[-1: : -1]]))
        if len(bin(reverse_x)) -2 >= 32: return 0
        return reverse_x*(-1) if x<0 else reverse_x

        
# @lc code=end

Solution().reverse(123) #321
Solution().reverse(-123) #-321
Solution().reverse(120) # 21