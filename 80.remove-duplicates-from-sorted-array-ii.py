#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n<2: return n
        index, occurence = 1, 1
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                occurence+=1
            else:
                occurence = 1
            if occurence <= 2:
                nums[index] = nums[i]
                index += 1
        return index

    def removeDuplicates_deprecate(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=2: return nums
        
        l, r= 0, 1 # nums 배열 왼쪽 이정표, 오른쪽 이정표
        flag = 0 # 현재 중복 숫자 최대 2개 조건 만족하는지 여부 판별 이정표
        val = nums[0] # 현재 기준 숫자
        flag = 0
        while r < n:
            print(f"{l}  {r}\n{nums}")
            if nums[l] == nums[r]:
                if flag == 0:
                    l+=1; r+=1
                    if val == nums[l]:
                        flag = 1
                else:
                    while nums[l] == nums[r]:
                        r+=1
                    print(f"  {l} {r}")
                    val = nums[r]
                    l += 1
                    nums[l] = nums[r]
                    flag = 0   
            else:
                val = nums[r]
                l += 1
                nums[l] = nums[r]
                flag = 0



# Solution().removeDuplicates([1,1,1,2,2,3])   
# Solution().removeDuplicates([0,0,1,1,1,1,2,3,3])  

# @lc code=end

