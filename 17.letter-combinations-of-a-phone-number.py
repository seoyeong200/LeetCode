#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        import string

        n = len(digits)
        if n < 1: return []

        # define dictionary that map the digit into possible alphabet       
        dix = {str(i):[] for i in range(2,10)}
        key = 2
        for s in string.ascii_lowercase:
            if s in ['d', 'g', 'j', 'm', 'p', 't', 'w']: key +=1
            dix[str(key)].append(s)

        
        answer = []
        stk = []
        # backtrack
        def backtrack(idx: int):
            if idx == n: 
                answer.append(''.join(stk))
                return
            for digit in dix[digits[idx]]:
                stk.append(digit)
                backtrack(idx+1)
                stk.pop()
        backtrack(0)
        return answer

Solution().letterCombinations("23")
# @lc code=end

