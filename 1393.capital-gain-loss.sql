--
-- @lc app=leetcode id=1393 lang=mysql
--
-- [1393] Capital Gain/Loss
--

-- @lc code=start
# Write your MySQL query statement below

select stock_name, sum(if(operation='Buy', price*(-1), price)) as capital_gain_loss
from Stocks
group by stock_name


-- @lc code=end

