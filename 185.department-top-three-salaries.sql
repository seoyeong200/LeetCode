--
-- @lc app=leetcode id=185 lang=mysql
--
-- [185] Department Top Three Salaries
--

-- @lc code=start
select Department, Employee, Salary
from (
select D.name as Department, E.name as Employee, E.salary as Salary, 
        dense_rank() over (partition by E.departmentId order by E.salary desc) as sal_rank
from Employee as E
left join Department as D on E.departmentId = D.id) as tbl
where sal_rank <= 3

-- @lc code=end

