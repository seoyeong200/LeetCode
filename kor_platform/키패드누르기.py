def solution(numbers, hand):
    """
    상하좌우 움직임, 1/4/7은 왼손, 3/6/9 오른손, 2/5/8/0 더 가까운 손
    (왼위치, 오른위치, 다음숫자)
    numbers 돌면서 hand
    """
    def get_distance(n1, n2):
        keypad = {
            '1': (0,0), '2': (0,1),'3': (0,2),
            '4': (1,0),'5': (1, 1),'6': (1, 2),
            '7': (2 ,0),'8': (2, 1),'9': (2, 2),
            '*': (3 ,0),'0': (3, 1),'#': (3, 2)
        }
        return abs(keypad[n1][0] - keypad[n2][0]) + \
            abs(keypad[n1][1] - keypad[n2][1])
    answer = ''
    hand = hand[0].upper()
    left, right = (1, 4, 7), (3, 6, 9)
    l, r = '*', '#'
    for number in numbers:
        if number in left: answer += 'L'
        elif number in right: answer += 'R'     
        else:
            diff = get_distance(str(l), str(number)) - get_distance(str(r), str(number))
            if diff < 0: answer += 'L'
            elif diff >0 : answer += 'R'
            else: answer += hand
        if answer[-1] == 'L': l = number
        else: r = number
            
    return answer







