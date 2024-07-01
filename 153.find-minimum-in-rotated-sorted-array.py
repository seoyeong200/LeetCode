#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[m] > nums[r]: 
                l = m+1
                """
                pivot/min value is occurred somewhere to the right of mid
                eg. [3 4 5 6 7 8 9 0 1 2]
                [r] is already smaller than [m] so [m] is no need to be considered
                """
            else:
                r = m
                """
                pivot was not encountered to the right of mid
                eg. [8 9 0 1 2 3 4 5 6 7]
                [m] is possibly the smallest value so r=m
                """
        return nums[l] # so the l index point at the smallest after the loop 


class Solution_mine:
    def findMin(self, nums: List[int]) -> int:
        """ runtime beats 20.83 %, memory usage beats 13.47 % (not efficient enough)
        l-m-r 이렇게 있을때 크기 순이 될 수 있는 경우들이
        (1, 2, 3) (3, 1, 2) (2, 3, 1) 즉
        순차증가(l<m<r), 제일 큰 수가 중간보다 덜 옴(m<r<l), 제일 큰 수가 중간보다 더 옴(r<l<m) 이렇게 존재할 수 있음
        -> 왼 탐색         -> 왼 탐색                     ->오른 탐색      
        """
        l, r = 0, len(nums)-1
        ans = 1e10
        while l<=r:
            print(l, r, ans)
            m = (l+r)//2
            if nums[r]<nums[l]<nums[m]: 
                ans = min(ans, nums[l], nums[m])
                l = m+1 # search right
            else: 
                ans = min(ans, nums[r], nums[m])
                r = m-1
        return ans

# ans = Solution().findMin([3,4,5,1,2])
ans = Solution().findMin([4,5,6,7,0,1,2])
# ans = Solution().findMin([11,13,15,17])
ans = Solution().findMin([5,1,2,3,4])
"""
단순 l, r 인덱스 값 비교해서 더 작은거 기준으로 왼쪽/오른쪽 탐색 범위 지정하면 
[5,1,2,3,4] 이런 케이스에서 왼쪽 탐색 아닌 오른쪽 탐색 범위로 설정됨
"""

print(ans)
# @lc code=end

