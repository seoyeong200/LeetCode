def solution(gems):
    answer = []
    uniq_cnt = len(set(gems))
    
    l, r = 0, 1
    while r <= len(gems):
        # r 움직여서 gem 추가, 갖고있는 gem 종류 다 만족하는지 확인
        if len(set(gems[l:r])) == uniq_cnt:
            # l 최대한 뒤로
            l += 1
            if len(set(gems[l:r])) != uniq_cnt:
                answer.append((r-l+1, [l, r]))
                r += 1
        else:
            r += 1
            
    return answer.sort(key=lambda x: (x[0], x[1][0]))[0][1]