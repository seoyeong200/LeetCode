def solution(board, aloc, bloc):
    n, m = len(board), len(board[0])
    
    def backtrack(x1, y1, x2, y2):
        if board[x1][y1] == 0: return 0
        board[x1][y1] = 0
        mov_cnt = 0
        
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx, ny = x1 + dx, y1 + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == 0: continue
            
            cnt = backtrack(x2, y2, nx, ny) + 1
            
            if mov_cnt % 2 == 0: # losing
                if cnt % 2 == 0: # lose again
                    mov_cnt = max(mov_cnt, cnt)
                else:           # win case !
                    mov_cnt = cnt
            else:               # winning
                if cnt % 2 ==1:
                    mov_cnt = min(mov_cnt, cnt)

        board[x1][y1] = 1
        return mov_cnt
    
    return backtrack(aloc[0], aloc[1], bloc[0], bloc[1])
    