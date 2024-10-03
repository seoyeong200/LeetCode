def solution(A):
    if len(A) == 2: return abs(A[0] - A[1])
    sum_l, sum_r = A[0], sum(A[1:])
    mindiff = abs(sum_l - abs(sum_r))
    for i in range(1, len(A)-1):
        sum_l += A[i]
        sum_r -= A[i]
        diff = abs(sum_l - sum_r)
        mindiff = min(mindiff, diff)

    return mindiff