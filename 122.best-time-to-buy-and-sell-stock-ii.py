#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
"""
[ Description ]
- prices[i] = price of a given stock on the ith day
- buy and/or sell stock
- can hold at most one share of the stock at any time
- can buy it then sell immediately on the same day
eg.
[7, 1, 5, 3, 6, 4]
buy at second day(1) and sell at third day(5) = 5-1
buy at fourth day(3) and sell at fifth day(6) = 6-3
-> profit = 4+3=7

[ Solution ]
- Greedy Algorithm is possible because you can sell/buy immediately that day
- buy(ith) whenever the profit can be gained the next day(i+1th)

"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum([max(0, x-y) for x,y in zip(prices[1:], prices[:-1])])

    def maxProfit_greedy(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                profit += (prices[i+1] - prices[i])
        return profit

# @lc code=end

