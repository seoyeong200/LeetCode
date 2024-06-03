--
-- @lc app=leetcode id=184 lang=mysql
--
-- [184] Department Highest Salary
--

-- @lc code=start

/*
departments 를 파티션으로 salary 순위를 매겨서 1위인 직원 이름과 부서 이름을 뽑는다.

*/
select Department, Employee, Salary
from (select D.name as Department, E.name as Employee,
    E.salary as Salary,
    rank() over (partition by departmentId order by salary desc) as sal_rank 
from Employee as E
left join Department as D on E.departmentId = D.id) as tbl
where sal_rank=1

-- @lc code=end

