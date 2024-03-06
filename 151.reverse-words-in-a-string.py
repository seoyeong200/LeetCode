#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
"""
"the sky is blue" -> "blue is sky the"
"  hello world  " -> "world hello"
"a good   example" -> "example good a"

 If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

"""
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().replace("  ", " ")
        start_idx = len(s) - len(s.split()[-1]); print(start_idx)
        for e in reversed(s.split()[:-1]):
            s += ' '+e

        s = s.replace(s[:start_idx], '')
        return s
# @lc code=end

