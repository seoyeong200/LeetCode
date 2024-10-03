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