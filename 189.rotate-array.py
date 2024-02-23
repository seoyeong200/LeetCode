#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
from typing import List


class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(l: int, r: int) -> None:
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1; r-=1
        n = len(nums)
        k%=n
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)
        

    def rotate_deprecate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        There are at least theee different ways to solve this problem.
        do it in-place (O(1)) extra space.

        """
        def get_dest_idx(idx) -> int:
            """
            0, 1, 2, 3 까지는 3, 4, 5, 6 즉 +k 하는 조건으로 들어가야지, 이게 idx<4 조건
            4, 5, 6이면 0, 1, 2 즉 -(k+1) 해줘야지
            """
            return idx+k if idx<n-k else idx-(n-k)
        
        def switch(idx1, idx2) -> None:
            tmp = nums[idx1]
            nums[idx1] = nums[idx2]
            nums[idx2] = tmp
        
        n = len(nums)
        k%=n
        if n < 2 or (n==2 and k%2==0): 
            return
        if n == 2:
            switch(0, 1)
            return

        i, dest_idx = 0, -1
        tmp1, tmp2 = nums[0], nums[get_dest_idx(0)]
        num_of_switch = 1
        print(num_of_switch, n)

        while dest_idx != 0:
            dest_idx = get_dest_idx(i)
            dest_dest_idx = get_dest_idx(dest_idx)
            if i == dest_dest_idx:
                if i == n//2: break
                print(nums)
                switch(i, dest_idx)
                i+=1
            else:
                print(i, dest_idx, nums, end='')
                nums[dest_idx] = tmp1
                tmp1 = tmp2
                tmp2 = nums[dest_dest_idx]
                print(nums)
                i = dest_idx
            num_of_switch+=1

# Solution().rotate([1,2,3,4,5,6,7], 3)
# Solution().rotate([1,2,3], 2)   
Solution().rotate([1,2,3,4,5,6,7], 3)     
# @lc code=end

