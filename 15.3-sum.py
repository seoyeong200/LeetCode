#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        - separate negative, positive element in dictionary, and count the number of zeros.
        - check if there's symmetric like (0, -1, 1) (0, -2, 2) etc.
        - iterate with set_a, set_b = neg, pos and set_a, set_b = pos, neg
            - iterate set_a items ) x1, q1
                - iterate sete_a_items[i:] ) x2, q2
                    - if (x1!=x2 or (x1==x2 and q1>1)) and -x1-x2 in set_b then append to the answer set

        Your runtime beats 99.53 % of python3 submissions (361 ms)
        Your memory usage beats 44.76 % of python3 submissions (21.1 MB)
        """
        from collections import defaultdict
        neg, pos, zero = defaultdict(int), defaultdict(int), 0
        for n in nums:
            if n > 0: pos[n] +=1
            elif n < 0: neg[n] +=1
            else: zero+=1

        ans = []
        if zero:
            for n in neg:
                if -n in pos: ans.append((n, 0, -n))
            if zero>=3: ans.append((0, 0, 0))
        
        for set_a, set_b in ((neg, pos), (pos, neg)):
            set_a_items = list(set_a.items())
            for i, (x1, p1) in enumerate(set_a_items):
                for x2, p2 in set_a_items[i:]:
                    if (x1!=x2 or (x1==x2 and p1>1)) and -x1-x2 in set_b:
                        ans.append((x1, x2, -x1-x2))
        return ans


    def threeSum_first(self, nums: List[int]) -> List[List[int]]:
        """
        Your runtime beats 33.58 % of python3 submissions (1026 ms)
        Your memory usage beats 6.89 % of python3 submissions (22.2 MB)
        """
        if len(nums) < 3: return []
        elif len(nums) == 3:
            if sum(nums) != 0: return []
            else: return [sorted(nums)]

        nums.sort(); print(nums)
        if nums[0] == nums[-1] == 0: return [[0, 0, 0]]
        elif nums[0]>=0 or nums[-1]<=0: return []

        n = len(nums)
        ans = set()
        for i in range(n-2):
            j, k = i+1, n-1
            
            while j<k:
                s = nums[i]+nums[j]+nums[k] 
                if s == 0:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif s>0: k-=1
                else: j+=1
        return [list(a) for a in ans]


            


ans = Solution().threeSum([0,1,1]); print(ans)
ans = Solution().threeSum([0,0,0]); print(ans)
ans = Solution().threeSum([-1,0,1,2,-1,-4]); print(ans)
# @lc code=end
        

