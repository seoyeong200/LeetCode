--
-- @lc app=leetcode id=586 lang=mysql
--
-- [586] Customer Placing the Largest Number of Orders
--

-- @lc code=start
-- order_number 횟수를 다 더하는게 아니라 주문이 발생한 횟수 를 더해야
with agg_orders as (
    select customer_number, count(order_number) as numof_orders
    from Orders
    group by customer_number
    order by numof_orders desc
)
select customer_number
from agg_orders
limit 1

-- @lc code=end

