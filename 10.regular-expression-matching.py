#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch_recursion(self, s: str, p: str) -> bool:
        """ s, p를 앞에서부터 비교해나가면서 이후 문자열을 재귀로 보내는 방식 
            9744 ms, 16.7 MB"""
        # p가 빈 문자열이면 -> s가 빈 문자열일때 True, 아니면 False
        if not p: return not s
        
        # s에 문자열이 남아있으면서 p[0]이 .또는s[0]인가?
        first_match = bool(s) and p[0] in {s[0], '.'}

        # len(p)가 2 이상이면서 p[1]이 *면 
            # p가 _*___ 이런식이라는거니까 ___ 얠 다시 recursion(s, p[2:])으로 확인한다.
            # 이거 만족 OR first_match 면서 recursion(s[1:], p)
        # 이게 아니라면 이제 0번째 이후인 문자열 [1:] 이랑 패턴 [1:]에 대해 재귀탐색
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch_recursion(s, p[2:]) or \
                first_match and self.isMatch_recursion(s[1:], p)
        else:
            return first_match and self.isMatch_recursion(s[1:], p[1:])


    def isMatch(self, s: str, p: str) -> bool:
        """이걸 dp[i][j]에 match(s[i:], p[j:])를 memoization 해서, string만드는 비싼 연산을 아끼고 중간 결과를 캐싱한다."""
        memo = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        memo[0][0] = True
        
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if s[i-1] == p[j-1] or p[j-1]=='.':
                    memo[i][j] = memo[i-1][j-1]; print(i, j, memo)
                elif p[j-1]=='*': 

                    if s[i-1]==p[j-2] or p[j-2]=='.':
                        memo[i][j] = memo[i][j-2] or memo[i][j-1]
                else:
                    memo[i][j] = False

        return memo[-1][-1]

        
    def isMatch_trial(self, s: str, p: str) -> bool:
        """
        . matches any single char
        * matches zero or more of the preceding elements
        """
        if p =='.*': return True
        for pre in p.split('*'):
            print(pre)
            if len(s)%len(pre) != 0: return False
            if ''.join(s.split(pre)) == '': return True
            if "." not in pre: return False
            for s1, s2 in zip(s, pre*(len(s)//len(pre))):
                if s1 != s2 and s2 != '.': return False
        return True



            
# @lc code=end

# ans1 = Solution().isMatch("aa", "a"); print(ans1)
# ans2 = Solution().isMatch("aa", "a*")
# ans3 = Solution().isMatch("ab", ".*")
# print(ans1, ans2, ans3)