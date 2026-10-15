# def solution(park, routes):
#     arr = []
#     sx = sy = 0
    
#     for i in range(len(park)):
#         if 'S' in park[i]:
#             sx = i
#             sy = park[i].index('S')
#         arr.append(list(park[i]))
        
#     for route in routes:
#         op, n = route.split(' ')
#         n = int(n)
        
#         if op == 'N':
#             nxt = sx - n
#             if nxt >= 0 and 'X' not in [a[sy] for a in arr[nxt:sx+1]]:
#                 sx = nxt  
#         elif op == 'S':
#             nxt = sx + n
#             if nxt < len(park) and 'X' not in [a[sy] for a in arr[sx:nxt+1]]:
#                 sx = nxt 
#         elif op == 'W':
#             nxt = sy - n
#             if nxt >= 0 and 'X' not in arr[sx][nxt:sy+1]:
#                 sy = nxt       
#         elif op == 'E':
#             nxt = sy + n
#             if nxt < len(park[0]) and 'X' not in arr[sx][sy:nxt+1]:
#                 sy = nxt
                
#     return [sx, sy]


def solution(park, routes):
    max_h, max_w = len(park), len(park[0])

    for i in range(max_h):
        if 'S' in park[i]:
            x = i
            y = park[i].index('S')

    for r in routes:
        op, n = r.split()
        n = int(n)

        if op == 'N':
            nxt = x - n
            if nxt >= 0 and 'X' not in [a[y] for a in park[nxt:x]]:
                x -= n
        elif op == 'S':
            nxt = x + n
            if nxt < max_h and 'X' not in [a[y] for a in park[x + 1:nxt + 1]]:
                x += n
        elif op == 'W':
            nxt = y - n
            if nxt >= 0 and 'X' not in park[x][nxt:y]:
                y -= n
        elif op == 'E':
            nxt = y + n
            if nxt < max_w and 'X' not in park[x][y + 1:nxt + 1]:
                y += n

    return [x, y]

print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]))