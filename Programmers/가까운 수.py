def solution(array, n):
    answer = []
    res = []
    
    for a in array:
        answer.append(abs(a - n))
        
    mn = min(answer)
    for i in range(len(answer)):
        if answer[i] == mn:
            res.append(array[i])
        
    return min(res)