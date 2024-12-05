def solution(t, p):
    ans = 0
    length = len(p)
    p = int(p)
    
    for i in range(0, len(t) - length + 1):
        if int(t[i:i+length]) <= p:
            ans += 1
            
    return ans