"""
      1    2       3   4
[[], [1], [3, 1], [], [3]]
      1    2   3        4           5    6     7     8    9   10     11     12
[[], [12], [], [5, 8], [11, 2, 8], [3], [10], [11], [3], [6], [11], [1, 9], [7]]

[3][5, 8][3]
visited 구조를 (fr, to) 로 갖기

붙어있는 노드 가장 많은 애가 생성 정점
생성 정점이 각 그래프의 시작 지점을 가리키고 있으니까 생성 정점이 갖고있는 노드 개수가 그래프 개수다.

그래프
cycle 이 있음
- 도넛 : 정점 n, 간선 n
아무 한 정점에서 출발해 이용한 적 없는 간선을 계속 따라가면 나머지 n-1개의 정점들을 한 번씩 방문한 뒤 원래 출발했던 정점으로 돌아옴
- 8자 : 정점 2n+1, 간선 2n+2
크기가 동일한 2개의 도넛 모양 그래프에서 정점을 하나씩 골라 결합시킨 형태

cycle이 없음
- 막대 : 정점 n, 간선 n-1
임의의 한 정점에서 출발해 간선을 계속 따라가면 나머지 n-1개의 정점을 한 번씩 방문하게 되는 정점이 단 하나 존재
"""
from collections import deque

# 사이클 판단 하면서 걍 다 돌아야겟는데.. 시간초과 나면 그렇게 하자
def graph_check(graph: list, start_v: int) -> int:
    q = deque([start_v])
    edge = set()
    vertex = set()
    while q:
        sv = q.popleft()
        vertex.add(sv)
        # 사이클 없음) 막대 그래프       
        if len(graph[sv]) == 0: return 2

        for nv in graph[sv]:
            if (sv, nv) not in edge:
                q.append(nv)
                edge.add((sv, nv))

    # 사이클 있으면서 간선 노드 수 같음) 도넛
    if len(edge) == len(vertex): return 1
    # 사이클 있으면서 같지 않음) 8자
    else: return 3

def solution(edges):
    print('\n', edges)
    answer = [0, 0, 0, 0] # 생성정점, 도넛수, 막대수, 8자수
    # 전체 노드 개수
    n = max([(max(l)) for l in edges])
    graph = [[] for _ in range(n+1)]
    for fr, to in edges:
        graph[fr].append(to)
    
    # 생성 정점 구하기
    max_linked = 0
    for i, g in enumerate(graph):
        if len(g) > max_linked:
            create_v = i
            max_linked = len(g)
    answer[0] = create_v

    # 각 시작 정점 보내서 어떤 그래프인지 판단하기
    for start_v in graph[create_v]:
        answer[graph_check(graph, start_v)] += 1
        
    return answer

solution([[2, 3], [4, 3], [1, 1], [2, 1]])
solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]])