--
-- @lc app=leetcode id=550 lang=mysql
--
-- [550] Game Play Analysis IV
--

-- @lc code=start
with tbl as (
    select player_id, min(event_date) as today, next_day
    from (select player_id, 
                event_date, 
                lead(event_date, 1) over(partition by player_id order by event_date) as next_day
        from Activity) as tbl1
    group by player_id
)


select round(count(*) / (select count(*) from tbl), 2) as fraction
from tbl
where datediff(next_day, today) = 1
-- @lc code=end

