--
-- @lc app=leetcode id=608 lang=mysql
--
-- [608] Tree Node
--

-- @lc code=start
/*
Input: 
Tree table:
+----+------+
| id | p_id |
+----+------+
| 1  | null |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
+----+------+
Output: 각 id 노드가 Root인지, Inner인지, Leaf인지 뽑기
+----+-------+
| id | type  |
+----+-------+
| 1  | Root  |
| 2  | Inner |
| 3  | Leaf  |
| 4  | Leaf  |
| 5  | Leaf  |
+----+-------+
*/

/*
root = p_id is null
leaf = id not in distanct(p_id)
inner = else
*/
select id, 
    case 
    when p_id is null then 'Root'
    when id in (select distinct(p_id) from Tree) then 'Inner'
    else 'Leaf'
    end as type
from Tree

-- 처은엔 leaf case롤 넣어서 not in 이면 leaf 값 갖도록 했는데 정상적으로 조건에 걸리지 않아서 실패했다.
-- null값이 포함되어있기 때문이다. 이렇게 구현하려면

select id,
    case when p_id is null then 'Root' 
        when id not in 
            (select p_id from tree where p_id is not null) 
            then 'Leaf' 
        else 'Inner' 
        end as type
from tree
-- 이런식으로 p_id에서 null 인 경우 빼주고 not in 조건 넣어줘야함

-- @lc code=end

