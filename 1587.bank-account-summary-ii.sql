--
-- @lc app=leetcode id=1587 lang=mysql
--
-- [1587] Bank Account Summary II
--

-- @lc code=start

select Users.name, sum(amount) as balance
from Transactions
group by account
having balance > 10000
left join Users on Users.account = Transactions.account
-- @lc code=end

