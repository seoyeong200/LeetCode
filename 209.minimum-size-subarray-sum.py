#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        return self.minSubArrayLen_most_efficient(target, nums)
    

    def minSubArrayLen_most_efficient(target: int, nums: List[int]) -> int:
        """
        개천재같은 풀이;;;
        범위 탐색이 아니라 앞에서부터 target 넘어갈때까지 누적합 하다가 target 도달하면 
        앞에서부터 sum 값 보면서 범위 좁혀보고 안되면 다음 loop 넘어가는 식으로 진행한다.
        """
        l, sm, ans, n = 0, 0, 1e10, len(nums) # left, sum, answer
        for r in range(n):
            sm += nums[r]
            while l<=r and sm>=target:
                ans = min(ans, r-l+1)
                sm -= nums[l]
                l+=1
        return 0 if ans==1e10 else ans


    def minSubArrayLen_with_bs(target: int, nums: List[int]) -> int:
        """ beats 6.62% time, 73.38% space
        시간복잡도 줄여야만 .. O(n log(n))
        이진탐색을 어디서 적용할 수 있는가?
        - 정렬 리스트) sum_arr : accumulative sum of nums
        - l을 n+1 범위에서 돌면서 시작점을 잡고, r 위치를 BS로 찾는다.
        """
        def binary_search(l: int, r: int, key: int) -> int:
            while l<=r:
                m = (l+r)//2
                if sum_arr[m]>=key: r=m-1
                else: l=m+1
            return l

        # [1] make accumulative sum of nums list
        n = len(nums)
        sum_arr = [0 for _ in range(n+1)]
        for i in range(1, n+1): sum_arr[i] += sum_arr[i-1]+nums[i-1]

        # [2] iterate n+1 and make startpoint, get endpoint via bs()
        # update ans as the minimum length
        ans = n+2
        for i in range(n+1):
            # 
            end = binary_search(i+1, n, sum_arr[i]+target)
            if end == n+1: break
            if end-i < ans: ans = end-i
        return 0 if ans==n+2 else ans
    

    def minSubArrayLen_time_exceed(target: int, nums: List[int]) -> int:
        """
        time limit exceed O(n^2)
        7, [2 3 1 2 4 3] 기준으로 보면 (2)(2,3)(2,3,1)(2,3,1,2) 
        이런식으로 가다가 7 되면 길이 업데이트하고 7 넘으면 다음으로 넘어가는 식
        """
        n = len(nums)
        ans = n
        for i in range(n):
            sub_sum = nums[i]
            if sub_sum >= target: return 1
            for j in range(i+1, n):
                sub_sum += nums[j]
                if sub_sum >= target: 
                    ans = min(ans, j-i+1)
                    break
        return 0 if ans==n else ans
                    
# @lc code=end

