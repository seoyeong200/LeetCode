#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        edge : next value of the candidate list
         - include or not
         - which means, it's binary tree, each vertex has exactly two child nodes
         - to avoid duplicated calculation, only consider next indices value (like i did in my Solution)
        vertex
         - sum of values that added from the so far path 
        """
        candidates.sort()
        result = []
        def backtrack(cur: list, pos: int, target: int):
            if target==0: 
                result.append(cur[:])
                return
            if target <=0: return

            prev = -1
            for i in range(pos, len(candidates)):
                candidate = candidates[i]
                if candidate <= prev: 
                    print(candidate, prev)
                    continue

                cur.append(candidate)
                backtrack(cur, i+1, target-candidate)
                cur.pop()
                prev = candidate

        backtrack([], 0, target)
        return result


    def combinationSum2_timeexceed(self, candidates: List[int], target: int) -> List[List[int]]:
        """time exceed
        edge: value that is about to include
        vertex: remained value to the target after include the value of the candidates"""
        
        """[1] stack result에 넣을 때 sort, 구분자 넣어서 string으로 만들고 result에 add"""
        stack, result = [], set() 
        candidates.sort()

        def backtrack(idx: int, remainder: int):
            """
            :idx: 호출한 함수에서 계산에 포함한 candidate index
            :remainder: 현재 target까지 남은 값
            """
            if remainder == 0:  # stack result에 넣어주기
                result.add(' '.join(sorted(stack)))
                return
            if remainder<0: return

            for i, candidate in enumerate(candidates[idx+1:]):
                    i += idx+1
                    if candidate > remainder: continue
                    stack.append(str(candidate))
                    backtrack(i, remainder-candidate)
                    stack.pop()

        backtrack(-1, target)
        # print(result)
        return [list(map(int, r.split())) for r in result]


    def combinationSum_dp(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        아까 풀었던 39번 문제에서 원소 중복으로 사용할 수 없는 조건만 더한 문제
        """
        candidates.sort()
        dp = [[] for _ in range(target+1)]

        for i, c in enumerate(candidates):
            if c>target: break # already bigger than target, no need to search for the combination sum
            i+=1
            # for j in range(i, len(candidates)): 
            for j in range(i, target+1):
                if j == i: dp[i].append([c])
                print(f"i={i}, c={c}, j={j}, cand[j]={candidates[j]}, dp={dp}")
                for comb in dp[candidates[j]-c]:
                    dp[i].append(comb + [c])


Solution().combinationSum2([10,1,2,7,6,1,5],8)
# Solution().combinationSum_BT([2,5,2,1,2], 5)
# Solution().combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 30)
# @lc code=end

