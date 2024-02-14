#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        """
        단순 조건절로 구현해보자
        """
        dix = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        comb_dix = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        # improve efficiency
        # don't need to make comb_dix
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        ans, flag, n = 0, False, len(s)
        for i, e in enumerate(s):
            if flag: 
                flag = False
                continue

            if e in ['I', 'X', 'C'] and i < n-1 and e+s[i+1] in comb_dix.keys():
                ans += comb_dix[e+s[i+1]]
                flag = True
            else:
                ans += dix[e]
        return ans


# @lc code=end

Solution().romanToInt("MCMXCIV")