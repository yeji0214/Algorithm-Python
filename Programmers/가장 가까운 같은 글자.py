def solution(s):
    answer = []
    
    for i in range(len(s)):
        c = s[i]
        if i > 0 and c in s[:i]:
            idx = s[:i][::-1].find(c)
            answer.append(idx + 1)
        else:
            answer.append(-1)
        
    return answer