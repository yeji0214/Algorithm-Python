def solution(array, commands):
    answer = []
    
    for c in commands:
        s, e, i = c[0], c[1], c[2]
        
        answer.append(sorted(array[s-1:e])[i-1])
        
    return answer