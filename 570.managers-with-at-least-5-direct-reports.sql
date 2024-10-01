--
-- @lc app=leetcode id=570 lang=mysql
--
-- [570] Managers with at Least 5 Direct Reports
--

-- @lc code=start
# Write your MySQL query statement below
select name
from Employee
where id in (
    select managerId
    from Employee
    where managerId is not null
    group by managerId
    having count(*) >= 5
)

-- @lc code=end

