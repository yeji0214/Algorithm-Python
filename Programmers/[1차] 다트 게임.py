import math

# 문제: 점수가 한 자리 수가 아닌 10이 나올수도 있음
def solution(dartResult):
    scores = []
    
    while dartResult:
        nxt_idx = 0
        opt = ''
        if len(dartResult) == 2 or (len(dartResult) == 3 and dartResult[2] == '0'):
            score, bonus = int(dartResult[0]), dartResult[1]
            nxt_idx = 2
            if bonus == '0':
                score, bonus = 10, dartResult[2]
                nxt_idx = 3
        elif dartResult[2] != '#' and dartResult[2] != '*':
            score, bonus = int(dartResult[0]), dartResult[1]
            nxt_idx = 2
            if bonus == '0':
                score, bonus = 10, dartResult[2]
                nxt_idx = 3
        else:
            score, bonus, opt = int(dartResult[0]), dartResult[1], dartResult[2]
            nxt_idx = 3
            if bonus == '0':
                score, bonus, opt = 10, dartResult[2], dartResult[3]
                nxt_idx = 4
        
        if bonus == 'D':
            score = math.pow(score, 2)
        elif bonus == 'T':
            score = math.pow(score, 3)

        if opt != '':
            if opt == '*':
                score *= 2
                if len(scores) > 0:
                    prev = scores.pop()
                    scores.append(prev * 2)
            else:
                score = -score

        scores.append(score)
                
        if nxt_idx >= len(dartResult):
            dartResult = ''
        else:
            dartResult = dartResult[nxt_idx:]
            
    return int(sum(scores))

print(solution("1D2S3T*"))