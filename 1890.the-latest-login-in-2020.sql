--
-- @lc app=leetcode id=1890 lang=mysql
--
-- [1890] The Latest Login in 2020
--
"""sub insight... 근데 막상 실행해보면 그냥 left쓰면 994ms, extract쓰면 1660ms 나옴;
In general, it would be efficient to write 
EXTRACT(YEAR FROM time_stamp) = 2020. 
This is because most database engines store date and time values internally as numeric data. 
Therefore, it is a lot easier for them 
to extract the "year" component with basic math operators 
compared to converting the entire column into a string format and then doing a substring search.
"""

-- @lc code=start
# Write your MySQL query statement below

select user_id, max(time_stamp) as last_stamp
from Logins
where left(time_stamp, 4) = '2020' 
group by user_id

-- @lc code=end

