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
    """
    같은 수 여러번 골라도 되는데 비내림차순
    """
    def recursion(string):
        x = 0 if string == '' else int(string[-1])
        if len(string) == m:
            print(' '.join(string))
            return
        for i in range(x, n+1):
            if i == 0: continue
            recursion(string + str(i))
    recursion('')

def n_m_5(n, m):
    """
    주어진 n개의 서로 다른 자연수 중 m개 고르는 수열.
    수열 사전 순으로 증가하는 순서로 출력해야 함

    앞에 12 13 14 21 23 24 31 32 34 41 42 43 만드는거랑 똑같은 케이스
    """
    # ********* 내 풀이 ***********
    lst = sorted(input().split())
    def recursion(string: str):
        """
        리스트 원소로 string 받는게 아니라, 지금 n에 8보다 작은 자연수니까
        리스트 인덱스 들고 다니다가 출력할때 실제 값으로 출력해야됨
        """
        if string in visited:
            return
        if len(string) == m:
            visited.add(string)
            print(' '.join([lst[int(s)] for s in string]))
            return
        
        iter = sorted(list(set([str(x) for x in range(n)]) - set(string)))
        for i in iter:
            recursion(string + str(i))
    visited = set()
    # recursion('')

    # ********* 풀이참고 ***********
    def recursion2(cur_seq: list):
        """
        :cur_seq: 선택한 값들을 담고있는 리스트
        """
        if len(cur_seq) == m:
            print(' '.join(map(str, cur_seq)))
            return 
        
        # 아직 선택됟지 않은 값들 중에서 차례대로 골라서 수열에 추가
        for i in range(len(lst)):
            if not visited[i]:
                visited[i] = True
                cur_seq.append(lst[i])
                recursion2(cur_seq)
                cur_seq.pop()
                visited[i] = False
    lst = sorted(list(map(int, input().split())))
    visited = [False] * n
    recursion2([])


def n_m_6(n, m):
    """
    n개 자연수 중 m개 고른 오름차순 수열 구하기
    """
    
    def recursion(cur_seq: list):
        if len(cur_seq) == m:
            print(' '.join(map(str, cur_seq)))
            return

        for i in range(len(cur_seq), len(lst)):
            if len(cur_seq) > 0 and cur_seq[-1] >= lst[i]: continue
            if visited[i]: continue
            visited[i] = True
            cur_seq.append(lst[i])
            recursion(cur_seq)
            cur_seq.pop()
            visited[i] = False

    lst = sorted(list(map(int, input().split())))
    visited = [False] * n
    recursion([])

# n, m = map(int, input().split())
n, m = 4, 4
n_m_6(n, m)
