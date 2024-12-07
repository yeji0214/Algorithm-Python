def solution(s):
    answer = []
    time = 0
    cnt = 0
    
    while s != '1':
        time += 1
        new_s = s.replace('0', '')
        cnt += len(s) - len(new_s)
        s = ''.join(list(bin(len(new_s)))[2:])
        
    answer.append(time)
    answer.append(cnt)
    
    return answer

print(solution("1111111"))