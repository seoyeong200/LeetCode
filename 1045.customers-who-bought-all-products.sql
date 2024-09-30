--
-- @lc app=leetcode id=1045 lang=mysql
--
-- [1045] Customers Who Bought All Products
--

-- @lc code=start
-- 효율 진짜 개박살
/* 전체 가능한 조합 생성해서 Customer 조인하고 null인거 뽑아서 전체 구매하지않은애 찾는게.. */
-- 근데 개박살까지는 아니네

with tbl1 as (
    select distinct(customer_id) as uniq_id from Customer
)

select uniq_id as customer_id
from tbl1
where uniq_id not in (
    select total_comb.id
    from (select tbl1.uniq_id as id, tbl2.product_key as product
        from tbl1
        cross join
            (select product_key from Product) as tbl2) as total_comb
    left join Customer 
    on total_comb.id = Customer.customer_id and total_comb.product = Customer.product_key
    where Customer.product_key is null
)



-- @lc code=end

