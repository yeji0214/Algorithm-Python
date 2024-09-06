def solution(k, m, score):
    answer = 0
    s = 0
    score = sorted(score, reverse=True)
    
    while s + m <= len(score):
        answer += min(score[s:s+m]) * m
        s += m
        
    return answer

# print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))