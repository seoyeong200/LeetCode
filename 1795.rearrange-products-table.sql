--
-- @lc app=leetcode id=1795 lang=mysql
--
-- [1795] Rearrange Products Table
--

-- @lc code=start
/*
rearrange the Products table so that each row has (product_id, store, price). 
If a product is not available in a store, do not include a row with that product_id and store combination in the result table.
Input: 
Products table:
+------------+--------+--------+--------+
| product_id | store1 | store2 | store3 |
+------------+--------+--------+--------+
| 0          | 95     | 100    | 105    |
| 1          | 70     | null   | 80     |
+------------+--------+--------+--------+
Output: 
+------------+--------+-------+
| product_id | store  | price |
+------------+--------+-------+
| 0          | store1 | 95    |
| 0          | store2 | 100   |
| 0          | store3 | 105   |
| 1          | store1 | 70    |
| 1          | store3 | 80    |
+------------+--------+-------+
*/

select *
from (
    select product_id, 
        case when store1 is not null then 'store1' end as store, 
        case when store1 is not null then store1  end as price
    from Products
    union
    select product_id, 
        case when store2 is not null then 'store2' end as store, 
        case when store2 is not null then store2  end as price
    from Products
    union
    select product_id, 
        case when store3 is not null then 'store3' end as store, 
        case when store3 is not null then store3  end as price
    from Products
) tbl
where store is not null

-- @lc code=end

