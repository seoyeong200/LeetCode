def solution(info, edges):
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
