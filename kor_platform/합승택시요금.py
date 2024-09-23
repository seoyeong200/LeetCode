"""
어느 지점까지 합승을 할것인가 가 관건인데, 완전탐색으로 다 해보면 된다,
합승 도착 지점을 경유지로 생각하고
    start에서 모든 지점(x))까지 최단경로
    + x에서 A 까지 최단경로
    + x에서 B 까지 최단경로
를 구하면 된다.
최단경로는 다익스트라 로도 구할 수 있겠지만, 어차피 구해야하는게
start -> 모든노드, 모든노드 -> A, 모든노드 ->B 이기 때문에, 플루이드와샬이 유리하다.
    - 경로 자체는 로깅해둘 필요 없이 요금만 필요하므로
    - 플루이드 와샬로 최단거리 값 구해놓고 계속 재사용하면 된다.
"""

def solution(n, s, a, b, fares):
    INF = 40000000
    # 최단 거리 배열을 2차원 리스트로 설정
    dist = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n): dist[i][i] = 0
    for edge in fares:
        dist[edge[0]-1][edge[1]-1] = edge[2]
        dist[edge[1]-1][edge[0]-1] = edge[2]
        
    def floyd():
        for k in range(n):          # 모든 경유지에 대해
            for i in range(n):      # 시작 지점 
                for j in range(n):  # 종료 지점
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

    floyd()

    s -= 1; a -= 1; b -= 1 
    answer = INF
    for k in range(n):
        answer = min(answer, dist[s][k] + dist[k][a] + dist[k][b])

    return answer   