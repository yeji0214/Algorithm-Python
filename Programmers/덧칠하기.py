def solution(n, m, section):
    answer = 0
    until = 0
    
    for s in section:
        if s > until:
            answer += 1
            until = s + m - 1
            
    return answer