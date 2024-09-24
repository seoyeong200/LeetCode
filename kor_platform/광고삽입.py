def solution_timeexceed(play_time, adv_time, logs):
    def to_sec(time):
        h, m, s = map(int, time.split(":"))
        return h*3600 + m*60 + s
    
    def to_timestr(sec):
        h, m, s = sec//3600, (sec%3600)//60, (sec%3600)%60
        return f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}"
    if play_time == adv_time: return '00:00:00'
    
    timeline = [0 for _ in range(to_sec(play_time))]
    start_points = []
    for log in logs:
        start, end = map(to_sec, log.split('-')) 
        start_points.append(start)
        for i in range(start, end): timeline[i] += 1
    
    start_points.sort()
    max_overlapped = -1
    adv_time = to_sec(adv_time)
    for start in start_points:
        overlapped_time = sum(timeline[start:start+adv_time])
        if max_overlapped < overlapped_time:
            max_overlapped = overlapped_time
            answer = start
    return to_timestr(answer)


"""
지금 start부터 end looping이 너무 비효율적이다.
[(t1, 's'), (t2, 'e'), (t3, 's'), ...] 이런식으로 만들어서 
첫번째 원소들을 정렬키로 해서 정렬하고, 
순차적으로 탐색하면서 's'이면 +1, 'e'면 -1하면서 제로썸처럼 오버래핑 개수를 팔로업하고,

"""