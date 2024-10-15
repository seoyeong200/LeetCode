"""
perm = 1~N 하나씩만 갖고있는 시퀀스
[4, 1, 3, 2] = perm -> ret 1
[4, 1, 3] != perm -> ret 0

"""

def solution(A):
    set_a = set(A)
    if len(A) != len(set_a) or \
        len(set([i+1 for i in range(len(A))]) - set_a) > 0:
        return 0
    return 1