def solution(a, b):
    answer = 0
    
    mx, mn = max(a, b), min(a, b)
    
    for i in range(mn, mx + 1):
        answer += i
        
    return answer