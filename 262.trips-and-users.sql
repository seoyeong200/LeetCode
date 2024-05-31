--
-- @lc app=leetcode id=262 lang=mysql
--
-- [262] Trips and Users
--

-- @lc code=start

/*
The cancellation rate is computed by 
    dividing the number of canceled (by client or driver) requests "with unbanned users" 
    by the total number of requests with unbanned users on that day.

Write a solution to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) 
each day between "2013-10-01" and "2013-10-03". 
Round Cancellation Rate to two decimal points.
*/

-- MORE EFFICIENT AND CLEAR SOLUTION
/*
1106ms, beats 52.92-74.91%
    가상테이블 따로 계속 만들지 말고 최대한 쿼리문 하나로 합치려고 하는게 필요하다.
    client_id, driver_id not banned, 기간 내 조건으로 뽑고
    바로 계산식 하면 됨
*/
select request_at as Day,
    round(sum(if(status = 'completed', 0, 1))/count(*), 2) as "Cancellation Rate"
from Trips
where client_id in (select user_id from Users where banned = 'No')
    and driver_id in (select user_id from Users where banned = 'No')
    and request_at between date("2013-10-01") and date("2013-10-03")
group by request_at

-- 1194ms, beats 38.89%

with unbanned_client as (
    select users_id as id
    from Users
    where banned = 'No' and role = 'client'
),
unbanned_driver as (
    select users_id as id
    from Users
    where banned = 'No' and role = 'driver'
),
in_date as (
    select id, client_id, driver_id, status, request_at
    from Trips
    where request_at between date("2013-10-01") and date("2013-10-03")
),
in_date__unbanned as (
    select T.id as id, T.status as status, T.request_at as request_at
    from in_date as T
    where T.client_id in (select id from unbanned_client)
    and T.driver_id in (select id from unbanned_driver)
),
cnt_by_status as (
    select sum(if(status = 'completed', 0, 1)) as cancelled_cnt,
            count(*) as total_cnt,
            request_at
    from in_date__unbanned
    group by request_at
)

select request_at as Day, round(cancelled_cnt/total_cnt, 2) as "Cancellation Rate"
from cnt_by_status


-- @lc code=end

