select name, bonus
from
    (select Employee.name as name, Bonus.bonus as bonus
    from Employee
    left join Bonus on Employee.empId = Bonus.empId) as bonus_amt
where bonus < 1000 or bonus is null

# Write your MySQL query statement below
select tbl1.name, Bonus.bonus
from
(select Employee.name as name, Employee.empId as empId
from Employee
where empId not in (select empId from Bonus where bonus>=1000)) as tbl1
left join Bonus on tbl1.empId = Bonus.empId