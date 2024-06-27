#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums [5,7,7,8,8,10] sorted in non-decreasing order, 
        find the "starting" and "ending" position([3,4]) of a given target value 8.

        If target is not found in the array, return [-1, -1].
        [5,7,7,8,8,10]
        target자체는 [5,7,8,10]에서 찾고 Position은 {5:1, 7:2, 8:3, 10:1}에서 계산
        {1, 3, 6, 7} 이런식으로 누적합으로 dic값 갖고와야하나..?

        """
        def find_diff_element(cur_pos, dir):
            pointer = cur_pos
            while 0<=pointer<len(nums) and nums[cur_pos] == nums[pointer]: pointer += dir
            return pointer
        
        def plain_bs():
            l, r = 0, len(nums)-1
            while l<=r:
                m = (l+r)//2 
                if target == nums[m]: return [find_diff_element(m, -1)+1, find_diff_element(m, 1)-1]
                elif target < nums[m]: r = m-1
                else: l = m+1
            return [-1, -1]
                
        """여기서도 find_range_point로 현재 nums[m] 이랑 같은 원소들 다 제끼는게 빠르려나?
        오히려 더 오래걸리네..."""
        def experiment_bs():
            l, r = 0, len(nums)-1
            while l<=r:
                m = (l+r)//2 
                if target == nums[m]: return [find_diff_element(m, -1)+1, find_diff_element(m, 1)-1]
                elif target < nums[m]: r = find_diff_element(m, -1)
                else: l = find_diff_element(m, 1)
            return [-1, -1]

        return plain_bs()


# @lc code=end

