def solution(k, tangerine):
    cnt = {}
    result = 0
    current_t = 0
    
    for t in tangerine:
        if t in cnt:
            cnt[t] += 1
        else:
            cnt[t] = 1
            
    cnt = dict(sorted(cnt.items(), key=lambda x: -x[1]))
    
    for key, value in cnt.items():
        current_t += value
        result += 1
        if current_t >= k:
            return result