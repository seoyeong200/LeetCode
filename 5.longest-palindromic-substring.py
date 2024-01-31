#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution_substring:
    """
    substring을 다 보내서 
    palindromic을 검사하는 메소드를 두고 substring을 다 보내본다
    - 큰 substring 부터 보내보면서 palindromic이면 바로 리턴
    """
    def palindromic(self, s):
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]: return False
        return True

    def longestPalindrome(self, s: str) -> str:
        """ 5184ms """
        n = len(s)
        for length in range(n, -1, -1):
            for i in range(n-length+1):
                substring = s[i:i+length]
                if self.palindromic(substring): return substring

class Solution:
    """ Dynamic Programming
    @ : Palindrome
    
    s[i:j] 가 @일때, s[i-1]==s[j+1] 이면 s[i-1:j+1] 또한 @이다.
    길이가 1인 문자열은 항상 @이다. 
    이 사실을 이용해 길이 3인 문자열부터 @인지 확인할 수 있다. 
        - 모든 j-i=2 인 모든 i, j쌍을 확인하면 된다.
    3짜리 @를 구했으면 이 사실을 이용해 5짜리 @, 이 사실을 이용해 7짜리 @를 구할 수 있다. and so on

    짝수 길이의 @
    - s[i]==s[i+1] 이면 s[i:i+1]은 @다.
    - 이를 계속 확장해서 4, 6, ..짜리 @를 구할 수 있다.

    n*n짜리 dp 배열을 두고, dp[i][j]에 (i, j) 범위의 substring이 @인지 여부 를 저장한다. 
    - 길이 1짜리 substring인 dp[i][i]를 True로 초기화한다.
    - 길이 2짜리 substring인 dp[i][i+1]을 s[i]==s[i+1] 로 초기화한다.
    - (i, j) pairs를 돌면서 dp 배열을 업데이트한다.
        - 길이 3짜리 substring부터, 즉 diff(i, j)==2 부터 시작해서
        - dp[i][j] = ( (s[i]==s[j]) && (dp[i+1][j-1]) ) 를 업데이트한다.
    """
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[ False for _ in range(n)] for _ in range(n)]
        ans = (0, 0)
        for i in range(n): dp[i][i] = True
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = (i, i+1)

        for diff in range(2, n):
            # i, i+diff 범위를 확인한다. 
            # 해당 범위 포인트의 문자열이 같고, 그 바로 안쪽 범위 문자열이 @인지 확인한다.
            for i in range(n-diff): 
                j = i + diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans = (i, j)
        i, j = ans
        return s[i:j+1]


# @lc code=end

