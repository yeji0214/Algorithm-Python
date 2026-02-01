def solution(storey):
    answer = 0
    
    while storey > 0:
        d = storey % 10
        if d < 5:
            answer += d
            storey //= 10
        elif d > 5:
            answer += (10 - d)
            storey = storey // 10 + 1
        else:
            if (storey // 10) % 10 >= 5:
                answer += (10 - d)
                storey = storey // 10 + 1
            else:
                answer += d
                storey //= 10
                
    return answer