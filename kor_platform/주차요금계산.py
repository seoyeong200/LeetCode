def solution(fees, records):
    from collections import defaultdict
    import math
    
    def calc_fare(time):
        if time <= fees[0]: return fees[1]
        return fees[1] + math.ceil((time-fees[0])/fees[2]) * fees[3]

    car_dic = defaultdict(int)
    flag = {'IN': -1, 'OUT': 1}
    parking_lot = set()
    for record in records:
        time, car_num, inout = map(str, record.split())
        h, m = map(int, time.split(':'))
        car_dic[car_num] += (h*60 + m) * flag[inout]
        if inout == 'IN':
            parking_lot.add(car_num)
        else:
            parking_lot.discard(car_num)
            
    for car in parking_lot:
        car_dic[car] += 23 * 60 + 59
        
    answer = []
    for car, culm_time in car_dic.items():
        answer.append((car, calc_fare(culm_time)))
    answer.sort(key=lambda x: x[0])
    return [fare for _, fare in answer]