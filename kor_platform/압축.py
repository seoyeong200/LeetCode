def solution(msg):
    """
    - 현재 인덱스 문자가 사전에 있음 -> 사전에 없을때까지 다음 문자 포함해서 검색
                    사전에 없음 -> 없는 문자 사전에 포함하고, 인덱스를 없던 곳 문자로 설정
            
    """
    dic = {}
    for idx, alp in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        dic[alp] = idx+1
    
    answer = []
    pt = 0
    n = len(msg)
    while pt < n: 
        for end_loc in range(pt+1, n):
            if msg[pt:end_loc+1] not in dic.keys():
                answer.append(dic[msg[pt:end_loc]])
                dic[msg[pt:end_loc+1]] = len(dic.keys())+1
                pt = end_loc
                break
        if msg[pt:] in dic.keys():
            answer.append(dic[msg[pt:]])
            break
    return answer