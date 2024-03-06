#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
"""
[ Description ]
- nums : sorted distinct value array
- is rotated to right
    - eg. [0,1,2,4,5,6,7] -> [4,5,6,7,0,1,2]
- return the index of target value (if its not in the array, return -1)
- solve it in O(logN) complexity

[ some O(log n) algorithms ]
1. binary search
2. divide and conquer
    - search, insert, delete in balanced binary search tree
    - merge sort (O(nlogn))
        - divide array in two : O(1)
        - merge two sorted arrays : O(n)
        - find two array that has to be divided : O(log n)
        - merge entire elements in each process : O(n)

[ Solution ]
- use binary search
- divide the condition into whether the left side is sorted or right side is sorted
    - if the left side is sorted side
        - left search when target in between (l,m]
        - right search otherwise
    - if the right side is sorted side
        - right search when target in between [m,r)
        - left search otherwise

[ Why am I get lost ]
- 현재 배열이 전체 정렬된 배열인지 아닌지르 먼저 따졌다
- left side, right side 정렬여부에 따라 탐색 범위를 바꿔주면 된다.

"""

# @lc code=start
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            m = (l+r)//2
            if target == nums[m]: return m

            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]: r = m-1
                else: l = m+1
            else:
                if nums[m] < target <= nums[r]: l = m+1
                else: r = m-1
        return -1
        


    def search_fail(self, nums: List[int], target: int) -> int:
        def bs(l, r):
            print(l, r)
            if l>=r: return -1

            m = (l+r)//2; mid = nums[m]
            if target == mid: return mid
            elif target == nums[l] : return l
            elif target == nums[r] : return r

            if nums[l] < nums[r]:
                bs(l+1, mid-1) if target < mid else bs(mid+1, r-1)

            else:
                """ it contains rotated subset 
                - mid > l (=left side sorted)
                    - target in left side condition ? target < mid
                    - target in right side condition ?
                        - like [9, 10, 0, 1, 2, 3]
                        - target > mid or target < r
                - mid < l (=right side sorted)
                    - target in left side condition ?
                        - like [6, 0, 1, 2, 3] [6, 7, 0, 1, 2]
                        - target < mid or target > l
                    - target in right side condition ?
                        - target > mid
                """
                if nums[r] < target < nums[l]: return -1
                else:
                    if mid > nums[l] :
                        if target < mid : bs(l+1, mid-1)
                        if target > mid or target < nums[r] : bs(mid+1, r-1)
                    else:
                        if target < mid or target > nums[l] : bs(l+1, mid-1)
                        if target > mid : bs(mid+1, r-1)
        return bs(0, len(nums)-1)



            
# @lc code=end
ans = Solution().search([4,5,6,7,0,1,2], 0); print(ans, '\n')
ans = Solution().search([4,5,6,7,0,1,2], 3); print(ans, '\n')
ans = Solution().search([1], 0); print(ans, '\n')
ans = Solution().search([1], 1); print(ans, '\n')
ans = Solution().search([4,5,6,7,8,1,2,3], 8); print(ans, '\n')
