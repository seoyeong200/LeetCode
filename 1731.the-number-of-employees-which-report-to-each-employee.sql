--
-- @lc app=leetcode id=1731 lang=mysql
--
-- [1731] The Number of Employees Which Report to Each Employee
--

-- @lc code=start
select tbl2.employee_id, tbl2.name, tbl1.reports_count, tbl1.average_age
from (select min(reports_to) as id, 
            count(reports_to) as reports_count,
            round(avg(age)) as average_age
        from Employees
        where reports_to is not null
        group by reports_to) as tbl1
left join 
    (select employee_id, name 
    from Employees) as tbl2 
on tbl1.id = tbl2.employee_id
order by tbl2.employee_id
-- @lc code=end

