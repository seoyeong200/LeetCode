#
# @lc app=leetcode id=306 lang=python3
#
# [306] Additive Number
#

# @lc code=start
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        from itertools import combinations as comb
        """solution
        i, j=1~n-1까지 둘로 쪼개는 조합
            -> a, b를 :i, i:j로 세팅해놓고,
            - 두 합이 j부터 시작하는 substring의 첫부분에 나오는지를 startswith() 내장함수로 채크
            - 
        """
        n = len(num)
        for i, j in comb(range(1, n), 2):
            a, b = num[:i], num[i:j]
            print(i, j, a, b)
            if a!=str(int(a)) or b!=str(int(b)): continue
            
            while j<n:
                twosum = str(int(a)+int(b))
                if not num.startswith(twosum, j): break
                j+=len(twosum)
                a, b = b, twosum
            if j == n: return True
        return False

    def isAdditiveNumber_failed(self, num: str) -> bool:
        """
        정확도 40/45  - 0235813 expected False
        """
        
        def backtrack(l: int, len1: int, len2: int):
            """
            :l: start point of two values
            :len1: length of left value x
            :len2: length of right value y
            """
            m, r = l+len1, l+len1+len2
            x, y = num[l:m], num[m:r]
            twosum = int(x)+int(y)
            print(x, y)
            # target value 확인할 것도 없이 이미 r이 n-1까지 올라감
            if r >= n: return False
            # twosum이 뒤에 남은 value 다 더한것과 같음, 
            target_val = num[r:]
            if twosum == int(target_val): 
                if x!=str(int(x)) or y!=str(int(y)) or target_val!=str(int(target_val)): return False
                return True

            next_len = 1

            while True:
                if r+next_len > n:
                    return False
                target_value = int(num[r:r+next_len])
                if twosum == target_value:
                    # x, y가 additive 만족. y, next_len으로 다음 additive number 찾기
                    return backtrack(m, len2, next_len)
                elif twosum < target_value:
                    # x, y로 additive 불가. 길이 조정해서 search
                    return backtrack(l, len1+1, len2) or \
                        backtrack(l, len1, len2+1) or \
                        backtrack(l, len1+1, len2+1)
                else:
                    # 아직 target_value가 x, y함한 값보다 작기 때문에, 길이 더 늘려서 확인 필요
                    next_len += 1


        n = len(num)
        if n<3: return False
        return backtrack(0, 1, 1)

ans = Solution().isAdditiveNumber("1023"); print(ans) # False
ans = Solution().isAdditiveNumber("101"); print(ans) # True
ans = Solution().isAdditiveNumber("112358"); print(ans) # True
# ans = Solution().isAdditiveNumber("199100199"); print(ans)
# @lc code=end

