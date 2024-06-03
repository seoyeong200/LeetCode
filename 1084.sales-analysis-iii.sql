--
-- @lc app=leetcode id=1084 lang=mysql
--
-- [1084] Sales Analysis III
--

-- @lc code=start
/*
Input: 
Product table:
+------------+--------------+------------+
| product_id | product_name | unit_price |
+------------+--------------+------------+
| 1          | S8           | 1000       |
| 2          | G4           | 800        |
| 3          | iPhone       | 1400       |
+------------+--------------+------------+
Sales table:
+-----------+------------+----------+------------+----------+-------+
| seller_id | product_id | buyer_id | sale_date  | quantity | price |
+-----------+------------+----------+------------+----------+-------+
| 1         | 1          | 1        | 2019-01-21 | 2        | 2000  |
| 1         | 2          | 2        | 2019-02-17 | 1        | 800   |
| 2         | 2          | 3        | 2019-06-02 | 1        | 800   |
| 3         | 3          | 4        | 2019-05-13 | 2        | 2800  |
+-----------+------------+----------+------------+----------+-------+
Output: 
+-------------+--------------+
| product_id  | product_name |
+-------------+--------------+
| 1           | S8           |
+-------------+--------------+
Explanation: 
The product with id 1 was only sold in the spring of 2019.
The product with id 2 was sold in the spring of 2019 but was also sold after the spring of 2019.
The product with id 3 was sold after spring 2019.
We return only product 1 as it is the product that was only sold in the spring of 2019.
*/
/*
한 product_id에서 여러번 팔릴 수 있고, 즉 여러 컬럼에서 여러 sale_date를 가질 수 있다.
모든 sale_date가 기간 범위 내에 있어야 조건을 만족하는 문제다.

sale_date 이 기간 내에 있지 않은 product_id를 뽑고,
이 id에 속하지 않은 것들만 Product에서 취한다.
*/
SELECT product_id, product_name
from Product
where product_id not in (select product_id 
                        from Sales 
                        where sale_date not between '2019-01-01' and '2019-03-31')
-- 이렇게 하면 Product 정보는 있지만 Sales에 데이터가 안잡혀있는 경우 기간에 관계없이 항상 그냥 포함되기 때문에,
and product_id in (select distinct(product_id) from Sales)


/* more optimized solution
- inner join으로 Sales에 없는 product 먼저 쳐내고
- product_id로 그룹화해서 sale_date 최대&최소값 모두 조건 범위 내에 있는 것들만 having으로 가져온다.
*/
SELECT p.product_id, p.product_name 
FROM Product AS p
INNER JOIN Sales AS s ON s.product_id = p.product_id
GROUP BY p.product_id
HAVING MAX(s.sale_date) BETWEEN '2019-01-01' AND '2019-03-31' 
AND MIN(s.sale_date) BETWEEN '2019-01-01' AND '2019-03-31'

-- @lc code=end

