--
-- @lc app=leetcode id=1070 lang=mysql
--
-- [1070] Product Sales Analysis III
--

-- @lc code=start

with tbl as (
    select product_id, min(year) as year
    from Sales
    group by product_id
)
select Sales.product_id, Sales.year as first_year, Sales.quantity, Sales.price 
from tbl
left join Sales
on Sales.product_id = tbl.product_id and Sales.year = tbl.year
-- @lc code=end

