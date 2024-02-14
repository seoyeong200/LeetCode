#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring_(self, s: str) -> int:
        """ 59 ms 16.9 MB """
        from collections import deque

        max_len = 0
        q = deque()
        for c in s:
            if c in q: 
                while q.popleft() != c: pass
            q.append(c)
            max_len = max(max_len, len(q))
        return max_len


    def lengthOfLongestSubstring(self, s: str) -> int:
        """ 40 ms 16.7 MB """
        n = len(s)
        if len(set(s)) == 1: return 1
        if n <= 2: return n

        left, right = 0, 1
        substring = set(s[left])
        max_len = 0

        while right < n:
            if s[right] in substring:
                max_len = max(max_len, right-left)
                while s[left]!=s[right]:
                    substring.remove(s[left])
                    left+=1
                left+=1
            else:
                substring.add(s[right])
            right+=1

        return max(max_len, right-left)

        
# @lc code=end

