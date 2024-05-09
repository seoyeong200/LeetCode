#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
from typing import List


class Solution:

    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        result = []

        def valid(x, y, z):
            """x, y, z stands for each separate position to make ip address"""
            octets = [s[:x], s[x:y], s[y:z], s[z:]]
            # check each a, b, c, d is valid for ip octect
            for octet in octets:
                if int(octet) < 0 or int(octet) > 255 or \
                (len(octet)>1 and octet[0] == '0'):
                    return
            result.append('.'.join(octets))

        def backtrack(cur: list, pos: int):
            if len(cur) == 3:
                valid(cur[0], cur[1], cur[2])
                return
            
            for i in range(pos, n):
                cur.append(i)
                backtrack(cur, i+1)
                cur.pop()
        backtrack([], 1)
        print(result)
        return result
        

Solution().restoreIpAddresses("25525511135")
Solution().restoreIpAddresses("0000")
Solution().restoreIpAddresses("101023")

# @lc code=end

