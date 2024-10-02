"""
처음 주어진 표의 상태를 비교하여 삭제되지 않은 행은 O, 삭제된 행은 X로 표시하여 문자열 형태로 return

"U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
"D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
"C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
    - 선택된 행 데이터 삭제되고 아래 있던 데이터들 한칸씩 올라옴
    - 마지막 행 삭제는 그냥 맨 뒤 데이터 날리고 앞 행 선택
"Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.
"""

def solution(n, k, cmd):
    def u_d_updown(op, x, k):
        """
        움직여야 하는 거리 x 범위 내에서 삭제된 노드 개수 더해서 k 계산
        min(0, k) or min(n, k) 리턴
        """
        if op == 'U':
            x *= (-1)
            k -= sum(deleted[k + x:k])
            k += x
            return 0 if k < 0 else k
        else:
            k += sum(deleted[k + 1: k + x + 1])
            k += x
            return n-1 if k >= n else k
    
    def c_delete(k):
        """
        del 처리 - log stacking, deleted[i]
        k 처리
        """
        log.append(k)
        deleted[k] = True
        return k-1 if k == n-1 else k+1
        
    def z_rollback(k):
        idx = log.pop()
        deleted[idx] = False
        # if idx < k:
        #     for i in range(k+1, n):
        #         if not deleted[i]: 
        #             return i       
        return k

    deleted = [False for _ in range(n)]
    log = []
    # print(k, [str(i) for i in range(n)])
    # print(k, ['T' if d else 'F' for d in deleted], log)
    for op in cmd:
        print(op)
        if op == "C":
            k = c_delete(k)
        elif op == "Z":
            k = z_rollback(k)
        else:
            k = u_d_updown(op.split()[0], int(op.split()[1]), k)
        # print(k, ['T' if d else 'F' for d in deleted], log)
    
    log = set(log)
    return ''.join(["X" if i in log else "O" for i in range(n)])