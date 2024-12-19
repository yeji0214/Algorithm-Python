def solution(n):
    candidate = [43046721, 14348907, 4782969, 1594323, 531441, 177147, 59049, 19683, 6561, 2187, 729, 243, 81, 27, 9, 3, 1]
    answer = 0
    three = ''
    idx = 0
    
    for i in range(len(candidate)):
        if n >= candidate[i]:
            idx = i
            break
            
    # 3진법 변환
    for i in range(idx, len(candidate)):
        three += str(n // candidate[i])
        n %= candidate[i]
    
    # 10진법으로 표현
    mul = 1
    for t in three:
        answer += (mul * int(t))
        mul *= 3
    
    return answer