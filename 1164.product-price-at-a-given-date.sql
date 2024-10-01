--
-- @lc app=leetcode id=1164 lang=mysql
--
-- [1164] Product Price at a Given Date
--

-- @lc code=start
with tbl1 as (
    select product_id, new_price as price
    from Products
    where (product_id, change_date) in (select product_id, max(change_date) as dt
                from Products
                where change_date <= "2019-08-16"
                group by product_id
            ) 
),
/*
| product_id | new_price |
| ---------- | --------- |
| 2          | 50        |
| 1          | 35        |
*/

tbl2 as (
    select distinct(product_id), 10 as price
    from Products
    group by product_id
    having min(change_date) > "2019-08-16"
)
/*
| product_id | price |
| ---------- | ----- |
| 3          | 10    |
*/

select * from tbl2
union 
select * from tbl1
-- @lc code=end

