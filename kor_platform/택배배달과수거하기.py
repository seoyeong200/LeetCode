def solution(cap, n, deliveries, pickups):

    answer = 0
    while deliveries or pickups: # 여기서 가장 많이 시간 줄어든다.
        while deliveries and deliveries[-1] == 0: # 뒤에 0인부분 날리기
            del(deliveries[-1])
        while pickups and pickups[-1] == 0:
            del[pickups[-1]]
        answer += max(len(deliveries), len(pickups)) * 2
        # 배달 
        cur_cap = cap
        for deliv_i in range(len(deliveries)-1, -1, -1):
            if deliveries[deliv_i] <= cur_cap: 
                cur_cap -= deliveries[deliv_i]
                deliveries[deliv_i] = 0
            else:
                deliveries[deliv_i] -= cur_cap
                break
        # 수거
        cur_cap = cap
        for pick_i in range(len(pickups)-1, -1, -1):
            if pickups[pick_i] <= cur_cap:
                cur_cap -= pickups[pick_i]
                pickups[pick_i] = 0
            else:
                pickups[pick_i] -= cur_cap
                break
        
    return answer


def solution_2(cap, n, deliveries, pickups):
    answer = 0
    most_far = n

    while sum(deliveries) + sum(pickups) > 0:
        deliv_cap, pick_cap = cap, cap
        for i in range(most_far-1, -1, -1):
            # deliv, pick 둘 다 뺄 수 있는 만큼 다 빼고 먼저 멈춘 인덱스 다음 탐색 인덱스 시작점으로 설정해주기
            if deliv_cap == 0: break

            if deliveries[i] <= deliv_cap: 
                deliv_cap -= deliveries[i]
                deliveries[i] = 0
            else:
                deliveries[i] -= deliv_cap

            if pickups[i] <= pick_cap: 
                pick_cap -= pickups[i]
                pickups[i] = 0
            else:
                pickups[i] -= pick_cap
        answer += most_far * 2
        most_far = i
    print(answer)
    return answer
            


solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])
solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0])