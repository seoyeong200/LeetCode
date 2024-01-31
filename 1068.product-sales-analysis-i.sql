--
-- @lc app=leetcode id=1068 lang=mysql
--
-- [1068] Product Sales Analysis I
--

-- @lc code=start
# Write your MySQL query statement below
select Product.product_name as product_name,
    Sales.year as year,
    Sales.price as price
from Sales
left join Product on Sales.product_id = Product.product_id
-- @lc code=end

