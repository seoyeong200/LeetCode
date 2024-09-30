--
-- @lc app=leetcode id=180 lang=mysql
--
-- [180] Consecutive Numbers
--

-- @lc code=start

/**
3번 연속되는지 확인 - lead
뒤로 1번째 == 현재 값 and 2번째 == 현재값 이ㅓㄱ
-> 걍 lead(num, 1) lead(num, 2) 하면 되는구나

+----+-----+
| id | num |x
+----+-----+
| 1  | 1   |0
| 2  | 1   |0
| 3  | 1   |0
| 4  | 2   |1
| 5  | 1   |2
| 6  | 2   |3
| 7  | 2   |3
+----+-----+
x로 group by, -> count, min(num) as num 가져와서 count>=3 인 num
숫자 달라질떼 +1씩 헤서 인덱스 만드는거 어케하지


**/

select distinct(num) as ConsecutiveNums
from (select num, 
            lead(num, 1) over() as num1, 
            lead(num, 2) over() as num2
        from Logs) as tbl
where num = num1 and num = num2
-- @lc code=end

