#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
from typing import List


class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        :people[i]: weight of ith person
        :limit: maximum weight that each boat can carry
        boat can carry up to two peoiple at the same time
        return minimum number of boats to carry evefy given person
        """
        people.sort()
        if len(people) <= 2: return 2 if sum(people)>limit else 1

        l, r = 0, len(people)-1 
        boat, present_weight = 0, 0

        while l<=r:
            if l == r: 
                boat+=1 
                break
            present_weight += people[l] + people[r]
            print(people[l] , people[r], present_weight)
            if present_weight <= limit: 
                """ ideal. initialize sum of wight and move on """
                present_weight = 0
                boat, l, r = boat+1, l+1, r-1
            else:
                """ limit exceed so add only [l] or [r], maybe neither"""
                if present_weight - people[r] <= limit: 
                    """ getting rid of smaller weight is not enough """
                    r-=1
                elif present_weight - people[l] <= limit: 
                    """ can make up one boat when contain only the heavier one """
                    l+=1
                boat+=1
                present_weight = 0

        return boat
                

Solution().numRescueBoats([1,1, 2, 3, 4, 4, 5, 9, 9, 9], 10)
Solution().numRescueBoats([1, 2], 3)
Solution().numRescueBoats([3, 2, 2, 1], 3)
Solution().numRescueBoats([3, 5, 3, 4], 5)


# @lc code=end

