#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start


from typing import List

class Solution_referencedBT:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        def dfs(cur, cur_sum, idx):                       # try out each possible cases
            if cur_sum > target: return                   # this is the case, cur_sum will never equal to target
            if cur_sum == target: ans.append(cur); return # if equal, add to `ans`
            for i in range(idx, n): 
                dfs(cur + [candidates[i]], cur_sum + candidates[i], i) # DFS
        dfs([], 0, 0)
        return ans        

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        candidate 원소를 이용해 dp의 각 인덱스 값을 만들 수 있는 segment 경우의 수 리스트를 저장한다.
        """
        dp = [[] for _ in range(target+1)]
        for c in candidates:
            #print(f"c={c}, dp={dp}")
            for i in range(c, target+1):
                if i == c: dp[c].append([c]) 
                # print(f"  i={i}, dp[i-c]={dp[i-c]}")
                for comb in dp[i-c]:
                    # print(f"    append {comb}+[{c}] in dp[{i}] ({dp[i]})")
                    dp[i].append(comb+[c])
            # print()
        return dp[-1] 

    """ dp execution prcedure
    c=2, dp=[[], [], [[2]], [], [], [], [], []]
        i=3, dp[i-c]=[]
        i=4, dp[i-c]=[[2]]
            append [2]+[2] in dp[4]([])
        i=5, dp[i-c]=[]
        i=6, dp[i-c]=[[2, 2]]
            append [2, 2]+[2] in dp[6]([])
        i=7, dp[i-c]=[]
        dp : [[], [], [[2]], [], [[2, 2]], [], [[2, 2, 2]], []]

    c=3, dp=[[], [], [[2]], [[3]], [[2, 2]], [], [[2, 2, 2]], []]
        i=4, dp[i-c]=[]
        i=5, dp[i-c]=[[2]]
            append [2]+[3] in dp[5]([])
        i=6, dp[i-c]=[[3]]
            append [3]+[3] in dp[6]([[2, 2, 2]])
        i=7, dp[i-c]=[[2, 2]]
            append [2, 2]+[3] in dp[7]([])
        dp : [[], [], [[2]], [[3]], [[2, 2]], [[2, 3]], [[2, 2, 2], [3, 3]], [[2, 2, 3]]]

    c=6, dp=[[], [], [[2]], [[3]], [[2, 2]], [[2, 3]], [[2, 2, 2], [3, 3], [6]], [[2, 2, 3]]]
        i=7, dp[i-c]=[]

    c=7, dp=[[], [], [[2]], [[3]], [[2, 2]], [[2, 3]], [[2, 2, 2], [3, 3], [6]], [[2, 2, 3], [7]]]
    """


    def combinationSum_mySolution(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        result에 순서만 바꾸면 중복인 케이스 스택 경우의 수를 제거하려고 stack을 string으로 만들어서 
        result set에 add 해주는 방식
        문제) stack 원소가 당연히 두자리 수 이상일 수 있음
        해결 방안1) join 할때 ''.join 말고 ' '.join 처럼 구분자를 넣어준다

        - visited로 이미 계산했던 값들은 다시 계산 안하도록 하려고 했는데,
            그렇게 구현할 경우 7, 4+3 이런 경우를 그냥 계산하지 않고 리턴해버려서 제외했다.
            방문처리로 올바르게 구현할 수도 있으려나..?
        """
        
        stack, result = [], set()
        def backtrack(remainder: int):
            if remainder == 0: 
                result.add(' '.join(sorted(stack)))
                return
            
            for candidate in candidates:
                if candidate <= remainder:
                    stack.append(str(candidate))
                    backtrack(remainder-candidate)
                    stack.pop()
            

        backtrack(target)
        # string으로 바꿔서 set칠까...
        # print(result)
        return [list(map(int, r.split(' '))) for r in result]
            
            
Solution().combinationSum([2,3,6,7], 7)



# @lc code=end

