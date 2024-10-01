--
-- @lc app=leetcode id=1934 lang=mysql
--
-- [1934] Confirmation Rate
--

-- @lc code=start
select tbl.user_id, COALESCE(round(tbl1.confirm_cnt / tbl2.each_cnt, 2), 0.00) as confirmation_rate
from Signups as tbl
left join (
    select user_id, count(*) as confirm_cnt
    from Confirmations
    where action = 'confirmed'
    group by user_id 
) as tbl1 on tbl.user_id = tbl1.user_id
left join(
    select user_id, count(*) as each_cnt
    from Confirmations
    group by user_id
) as tbl2 on tbl.user_id = tbl2.user_id
-- @lc code=end

