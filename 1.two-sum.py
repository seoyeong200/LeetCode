#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
"""
두개를 더해서 target이 되는 두 숫자의 인덱스 리턴하는 문제
- O(n^2)보다 적은 TC로 풀기 위해선?
- target 9-x 저장해넣고 [2,7,11,15] [7, 2, -2, -6]
    - 
"""

# @lc code=start
from typing import List


class Solution:
    def twoSum_brute_force(self, nums: List[int], target: int) -> List[int]:
        """
        1662ms
        """
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target: return [i, j]
        return -1

    def twoSum_hashing(self, nums: List[int], target: int) -> List[int]:
        '''
        51ms
        각 num에 대해서 target-n이 배열에 있는지, 어딨는지를 알아야함
        - 각 num의 target-n이 hashing 가능하도록 n:i를 저장해놓고
        - num돌면서 해싱해보고 있으면 바로 리턴하면 되겟다
        '''
        dic = { n:i for i, n in enumerate(nums)}
        for i in range(len(nums)):
            try: 
                pair_idx = dic[target-nums[i]]
                if i != pair_idx: return [i, pair_idx]
            except:
                pass
        
# @lc code=end
