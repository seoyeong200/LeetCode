#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        """
        - make left , right pointer
        - left pointer indeicates the lowest price
        - if left pointed valud is smaller than right pointed value, update max profit and increment right pointer by 1
        - otherwise, left pointer is now point right pointed value and increment right pointer by 1
        """
        n = len(prices)
        if n < 2: return 0
        if n == 2: return max(0, prices[1] - prices[0])

        left, right = 0, 1
        max_profit = 0
        while right < n:
            if prices[left] < prices[right]:
                max_profit = max(max_profit, prices[right]-prices[left])
            else:
                left = right
            right+=1
        return max_profit

    def maxProfit_simpliest(self, prices: List[int]) -> int:
        """
        prices = [542, 387, 276, 740, 420, 282, 531, 750, 466, 295, 503, 36, 362, 83, 578, 524]
        accumulate(prices, min)
               = [542, 387, 276, 276, 276, 276, 276, 276, 276, 276, 276, 36, 36, 36, 36, 36]
        """
        from itertools import accumulate

        return max(j - k for j,k in zip(prices, accumulate(prices,min)))

    def maxProfit_deprecate(self, prices: List[int]) -> int:
        """
        너무 오래걸리는듯
        """
        n = len(prices)
        if n < 2: return 0
        if n == 2: return max(0, prices[1] - prices[0])

        ans = []        
        for i, p_price in enumerate(prices[:-1]):
            ans.append(max(prices[i+1:]) - p_price)
        # print(max(ans), ans)
        return max(0, max(ans))

# @lc code=end
test = [542,387,276,740,420,282,531,750,466,295,503,36,362,83,578,524,812,645,821,74,505,65,519,181,598,121,710,45,311,56,824,334,252,169,426,179,122,689,244,872,549,138]
Solution().maxProfit(test)


