def solution(park, routes):
    arr = []
    sx = sy = 0
    
    for i in range(len(park)):
        if 'S' in park[i]:
            sx = i
            sy = park[i].index('S')
        arr.append(list(park[i]))
        
    for route in routes:
        op, n = route.split(' ')
        n = int(n)
        
        if op == 'N':
            nxt = sx - n
            if nxt >= 0 and 'X' not in [a[sy] for a in arr[nxt:sx+1]]:
                sx = nxt  
        elif op == 'S':
            nxt = sx + n
            if nxt < len(park) and 'X' not in [a[sy] for a in arr[sx:nxt+1]]:
                sx = nxt 
        elif op == 'W':
            nxt = sy - n
            if nxt >= 0 and 'X' not in arr[sx][nxt:sy+1]:
                sy = nxt       
        elif op == 'E':
            nxt = sy + n
            if nxt < len(park[0]) and 'X' not in arr[sx][sy:nxt+1]:
                sy = nxt
                
    return [sx, sy]
                