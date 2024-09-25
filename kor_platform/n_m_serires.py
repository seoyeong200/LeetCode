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

    visited = set()
    recursion('', set([i for i in range(1, n+1)]))


def n_m_2(n, m):
    """
    1부터 n까지 자연수 중에서 중복없이 m개 고르는데 수열이 오름차순이어야됨
    - 다음 재귀에서 숫자가 작아질 일이 없으니까 리스트로 다음 값 후보를 계속 들고다닐거없이
    - 그냥 현재 값 기준으로 증가시키면서 다음 노드 호출하면 될 것 같음
    - dfs. 
    """
    def recursion(string: str):
        x = 0 if string == '' else int(string[-1])
        if string in visited: return
        if len(string) == m:
            print(' '.join(string))
            visited.add(string)
            return
        if x == n: return

        for i in range(x+1, n+1):
            recursion(string + str(i))

    visited = set()
    recursion('')

def n_m_3(n, m):
    """
    같은 수를 여러번 골라도되는 1-n 중 m개 고른 수열
    """
    def recursion(string: str):
        if len(string) == m:
            print(' '.join(string))
            return
        for i in range(1, n+1):
            recursion(string + str(i))

    recursion('')

def n_m_4(n, m):
    pass

def n_m_5(n, m):
    lst = list(map(int, input()))
    pass

# n, m = map(int, input().split())
n, m = 3, 3
# print(f"n={n} m={m}")
n_m_3(n, m)