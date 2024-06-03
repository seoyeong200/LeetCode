--
-- @lc app=leetcode id=178 lang=mysql
--
-- [178] Rank Scores
--

-- @lc code=start
/*
Input: 
Scores table:
+----+-------+
| id | score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
*/
select score, rank() over (order by score desc) as 'rank'
from Scores
/*
| score | rank |
| ----- | ---- |
| 4     | 1    |
| 4     | 1    |
| 3.85  | 3    |
| 3.65  | 4    |
| 3.65  | 4    |
| 3.5   | 6    |
*/

select score, dense_rank() over (order by score desc) as 'rank'
from Scores
/*
dense_rank : 동일
| score | rank |
| ----- | ---- |
| 4     | 1    |
| 4     | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.5   | 4    |
*/

-- @lc code=end

