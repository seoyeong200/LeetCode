#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        basic binary search problem
        - sorted array is given
        - distinct elements
        - point: find the POSITION(index) of the list that the target would be inserted in a sorted order
        - O(logn) complexity

        이진탐색 갈기다가 자기보다 크거나 같은 수 발견하면 해당 인덱스 리턴하면 됨
        - 만약 그런 수 발견 못하고 while 빠져나왔다고 하면 
        - target이 리스트에서 제일 크다는거니까 len return 
        """

        l, r  = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if target == nums[m]: return m
            # 탐색 범위 조정
            elif target < nums[m]: r = m-1
            else: l = m+1
        return l
        

        
# @lc code=end

