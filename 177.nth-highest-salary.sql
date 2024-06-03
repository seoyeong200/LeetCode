--
-- @lc app=leetcode id=177 lang=mysql
--
-- [177] Nth Highest Salary
--

-- @lc code=start
/*
find the nth highest salary from the Employee table. 
If there is no nth highest salary, return null.
Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+

동일 순위가 있을 때 해당 순위 값의 개수만큼 rank값을 뛰어넘는 rank()로 하게 되면 
값 자체의 n번째 순위 값을 볼 수 없게 된다.
따라서 동일 순위 중복에 관계없이 순위가 uniformly increasing되는 dense_rank를 이용해야 한다.
*/
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
        select distinct(salary)
        from(
            select salary, dense_rank() over (order by salary desc) as salary_rank 
            from Employee
        ) rank_tbl
        where salary_rank = N
  );
-- @lc code=end

