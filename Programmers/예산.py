def solution(d, budget):
    answer = 0
    total = 0
    
    sorted_d = sorted(d)
    
    for b in sorted_d:
        total += b
        if total <= budget:
            answer += 1
        else:
            return answer
            
    return answer