#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
"""
[ Description ]
nums1, nums2 - non-decreasing order
- m(n) = number of elements in nums1(nums2)
- merge nums1, nums2 in non-decreasing order
- eg. nums1 = [1,2,3,0,0,0], nums2 = [2,5,6] -> [1,2,2,3,5,6]
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0: 
            for i in range(n): nums1[i] = nums2[i]
            return 

        if m==1 and n==1:
            min_, max_ = min(nums1[0], nums2[0]), max(nums1[0], nums2[0])
            nums1[0], nums1[1] = min_, max_
            return

        p1, p2, p3 = m-1, n-1, len(nums1)-1

        while p1 >= 0 and p2 >=0:
            if nums1[p1] <= nums2[p2]:
                nums1[p3] = nums2[p2]
                p2-=1
            else:
                nums1[p3] = nums1[p1]
                p1-=1
            p3-=1

        for i in range(p2+1): nums1[i] = nums2[i]
        
        



Solution().merge([1,2,3,0,0,0], 3, [2, 5, 6], 3)
# Solution().merge([0], 0, [1], 1)
Solution().merge([2, 0], 1, [1], 1)
# @lc code=end

