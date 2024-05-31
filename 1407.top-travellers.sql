--
-- @lc app=leetcode id=1407 lang=mysql
--
-- [1407] Top Travellers
--

-- @lc code=start
# Write your MySQL query statement below
select U.name as name , coalesce(R.distance, 0) as travelled_distance
from Users as U
left join (
    select user_id, sum(distance) as distance
    from Rides 
    group by user_id) as R 
on U.id = R.user_id
order by travelled_distance desc, name asc


-- @lc code=end

