--
-- @lc app=leetcode id=1667 lang=mysql
--
-- [1667] Fix Names in a Table
--

-- @lc code=start
/*
1. 
left 첫번째(left(string, 1)) 대문자(upper()), 나머지 소문자롤 바꾸기
2. 
정규식 써서 ?
-> MySQL에서 정규식 사용 제한
MySQL에서는 기본적으로 REGEXP를 사용하여 문자열을 검색할 수 있지만, 문자열 변환에는 직접 사용할 수 없습니다. 
따라서 문자열 변환 작업은 CONCAT, UPPER, LOWER 등의 함수를 조합하여 처리하는 것이 좋습니다.
*/
--1,
select user_id, 
    concat(upper(left(name, 1)), lower(substring(name, 2))) as name
from Users
order by user_id
-- @lc code=end

