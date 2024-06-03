--
-- @lc app=leetcode id=1729 lang=mysql
--
-- [1729] Find Followers Count
--

-- @lc code=start
select user_id, min(cnt) as followers_count
from (
    select user_id, count(*) over (partition by user_id) as cnt
    from Followers) as t
group by user_id

/*window 궂이 안써도 그룹바이 쳐서 distinct 뽑으면 된다.....*/

select user_id, count(distinct(followers_count))
from Followers
group by user_id
-- @lc code=end

