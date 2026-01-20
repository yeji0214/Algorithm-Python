def solution(record):
    nickname = {}
    result = []
    
    for r in record:
        r = r.split()
        
        if r[0] == 'Enter' or r[0] == 'Change':
            nickname[r[1]] = r[2]
            
    for r in record:
        r = r.split()
        
        if r[0] == 'Enter':
            result.append(f'{nickname[r[1]]}님이 들어왔습니다.')
        elif r[0] == 'Leave':
            result.append(f'{nickname[r[1]]}님이 나갔습니다.')
            
    return result