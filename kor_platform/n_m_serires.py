def n_m_1(n, m):
    """
    1부터 n까지 자연수 중에서 중복없이 m개 고른 수열 
    n^(m)
    """
    def recursion(string: str, avail_lst: set):
        # print(string, avail_lst)
        if string in visited: return

        if len(string) == m:
            print(' '.join(string))
            visited.add(string)
            return
        
        if len(avail_lst) == 0: return
        lst = sorted(list(avail_lst))
        for i in lst:
            avail_lst.discard(i)
            recursion(string + str(i), avail_lst)
            avail_lst.add(i)
            # recursion(string, avail_lst)

    visited = set()
    recursion('', set([i for i in range(1, n+1)]))


def n_m_2(n, m):
    pass

def n_m_3(n, m):
    pass

def n_m_4(n, m):
    pass

def n_m_5(n, m):
    lst = list(map(int, input()))
    pass

n, m = map(int, input().split())
# n, m = 4, 4
# print(f"n={n} m={m}")
n_m_1(n, m)