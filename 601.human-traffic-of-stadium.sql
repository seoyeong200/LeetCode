--
-- @lc app=leetcode id=601 lang=mysql
--
-- [601] Human Traffic of Stadium
--

-- @lc code=start
/*
- the records with three or more rows with consecutive id's
- the number of people is greater than or equal to 100 for each.
| 2    | 2017-01-02 | 1
| 3    | 2017-01-03 | 2
| 5    | 2017-01-05 | 1
| 6    | 2017-01-06 | 2
| 7    | 2017-01-07 | 3
| 8    | 2017-01-09 | 4

LEAD, LAG : 행 기준 이전행/다음행 값 참조하기
LEAD(): 현재 행에서 지정한 오프셋만큼 '뒤'에 있는 행의 값을 반환
    LEAD(column_name, offset, default_value) 
        OVER (PARTITION BY partition_column ORDER BY order_column)

LAG(): 현재 행에서 지정한 오프셋만큼 '앞'에 있는 행의 값을 반환
    LAG(column_name, offset, default_value) 
        OVER (PARTITION BY partition_column ORDER BY order_column)

    - offset: 뒤로 몇 번째 행의 값을 참조할지 지정 (기본값은 1)
    - default_value: 참조할 값이 없는 경우 사용할 기본값 (기본값은 NULL)
    - PARTITION BY: 윈도우를 나누는 기준
*/
select id , visit_date, people
from (
    select id , visit_date, people,
        if(
            id+2=lead(id, 2) over() or 
            id-2=lag(id, 2) over (), true, false) as three_day_condition
    from Stadium
    where people>=100
) as tbl
where three_day_condition = 1

-- 이렇게 하니까 중간에 껴있는 데이터 날라감

select id , visit_date, people,
    if(id+2=lead(id, 2) over(), true, false) as at_least_three,
    if(id-1=lag(id, 1) over(), true, false) as consecutive
from Stadium
where people>=100


/**************Solutions**********/


-- @lc code=end

