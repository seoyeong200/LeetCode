"""
N counters
- 초기값 0
- increase(X) = counter X 1 증가
- max counter = 모든 counter 값이 해당 시점 counter 최댓값으로
A
- 길이 M 배열, 각 원소 [1, N+1] 범위
- A[i] 가 N 이하면 increase, N+1이면 max operation 수행한다.

A [3, 4, 4, 6, 1, 4, 4], N=5
. (0, 0, 0, 0, 0)
3 (0, 0, 1, 0, 0) 
4 (0, 0, 1, 1, 0)
4 (0, 0, 1, 2, 0) 
6 (2, 2, 2, 2, 2)
1 (3, 2, 2, 2, 2)
4 (3, 2, 2, 3, 2)
4 (3, 2, 2, 4, 2)
"""

def solution_time_exceed(N, A):
    counter = [0] * N
    max_cnt = 0
    for i in range(len(A)):
        if A[i] == N+1:
            counter = [max_cnt for _ in range(N)]
        else:
            counter[A[i]-1] += 1
            max_cnt = max(max_cnt, counter[A[i]-1])
    return counter

def solution(N, A):
    from collections import Counter

    max_log = []
    increase_ops = ''.join(list(map(str, A))).split(str(N+1))

    for x in increase_ops:
        if x == '': continue # max operation 붙어있거나 그걸로 끝나는 경우
        dix = dict(Counter(x))
        max_log.append(max(dix.values()))

    # max op 으로 끝난 경우 처리
    last_op_result = max_log.pop()
    if A[-1] == N+1: return [last_op_result[-1]] * N

    # max operation이 존재했었음
    if max_log: 
        ans = [max_log[-1]] * N
    # max operation이 존재하지 않았었음
    else:
        ans = [0] * N
    for key, val in dix.items():
        ans[int(key)-1] += val

    return ans