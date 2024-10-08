"""
각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.
"""
def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    # 각 id의 [나를신고한사람리스트]
    reported = {id: set() for id in id_list}
    report = list(set(report))
    
    for r in report:
        fr, to = map(str, r.split())
        reported[to].add(fr)
    
    idx_id = {id: i for i, id in enumerate(id_list)}
    
    for val in reported.values():
        if len(val) >= k:
            for id in val:
                answer[idx_id[id]] += 1
    
    return answer