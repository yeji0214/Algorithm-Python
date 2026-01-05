def solution(s):
    sets = []
    result = []
    
    s = s[2:-2]
    s = s.split('},{')
    
    for S in s:
        sets.append(set(map(int, S.split(','))))
        
    sets = sorted(sets, key=len)
    result.append(list(sets[0])[0])
    
    for i in range(1, len(s)):
        result.append(list(sets[i] - sets[i - 1])[0])
        
    return result