def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for p, c in edges:
        graph[p].append(c)
        graph[c].append(p)
    
    def backtrack(sv, s, w):
        global maxS
        # 방문처리
        if visited[sv][s][w]: return
        visited[sv][s][w] = True
        
        # 양, 늑대 개수, 노드 상태 처리
        # 현재 양인지 늑대인지(info[sv])도 같이 백업하고 양/늑대 개수 계산한 후에
        # -1로 방문처리하는데.. 그럴거면 visited 3차원으로 왜 만든거지.. 일단 해보고 나중에 돌아오기
        # 아 왔던 노드 다시 또 올 수 있는데 그때는 양/늑대 이미 셌으니까 또 셀 필요가 없구나
        s_backup, w_backup, node_backup = s, w, info[sv]
        if info[sv] == 0: 
            s += 1
        elif info[sv] == 1: 
            w += 1
        info[sv] = -1
        
        # 이후 탐색 보내기
        if w < s:
            maxS = max(maxS, s)
            for nv in graph[sv]:
                backtrack(nv, s, w)
        info[sv] = node_backup
        visited[sv][s_backup][w_backup] = False
    
    global maxS
    maxS = 0
    wolf_total = sum(info)
    sheep_total = len(info) - wolf_total
    visited = [[
                [False for _ in range(18)] for _ in range(18)
            ] for _ in range(17)
        ]
    backtrack(0, 0, 0)
    
    return maxS


def solution_fail(info, edges):
    graph = [[] for _ in range(len(info))]
    for p, c in edges:
        graph[p].append(c)
    
    def backtrack(sv, candidate, s, w):
        if info[sv] == 0: s += 1
        else: w += 1
        if s == w: s = 0
        
        if (s == len(info) - sum(info)) or \
            (len(candidate) == 0 and len(graph[sv]) == 0):
                return s

        candidate += graph[sv].copy()
            
        for nv in candidate:
            candidate.pop()
            s = max(s, backtrack(nv, candidate, s, w))
            candidate.add(nv)
        return s
    visited = [False]*len(info)
    
    return backtrack(0, [], info[0]==0, info[0]==1)
