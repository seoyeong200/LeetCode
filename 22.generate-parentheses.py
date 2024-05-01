#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, result = [], []

        def backtrack(openN: int, closedN: int):
            if openN == closedN == n:
                result.append(''.join(stack))
                return 
            
            if openN < n:
                stack.append('(')
                backtrack(openN+1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(')')
                backtrack(openN, closedN+1)
                stack.pop()

        backtrack(0, 0)
        return result



    def generateParenthesis_mySolution(self, n: int) -> List[str]:
        from collections import Counter
        def recursion(string: str):
            o, c = Counter(string).get('('), Counter(string).get(')')
            open, close = o if o else 0, c if c else 0
            if open == n and close == n: answer.append(string)

            if open < n: recursion(string+'(')
            if close < open: recursion(string+')')
        answer = []
        recursion("(")
        return answer

        
# @lc code=end

