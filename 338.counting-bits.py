#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
"""
ans[i] : i를 이진수로 나타냈을 때 1 개수
- 0<= i <=n
0   0       0  0
1   1       1  1


2   10      1  0+1
3   11      2  1+1


4   100     1  0+1
5   101     2  1+1
6   110     2  0+1+1
7   111     3  1+1+1


8   1000    1  0+1
9   1001    2  1+1
10  1010    2  0+1+1
11  1011    3  1+1+1

12  1100    2  0+1+1
13  1101    3  1+1+1
14  1110    3  0+1+1+1
15  1111    4  1+1+1+1

16  10000
...
[]
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0, 1]
        if n < 2: return ans[:n+1]
        idx = 2
        while n >= idx*2:            
            ans += [x+1 for x in ans]
            idx = idx*2 # 4, 8, 16, 32, ...
            
        return ans+[x+1 for x in ans[:n+1 - len(ans)]]

        
# @lc code=end
ans = Solution().countBits(8); print(ans)


