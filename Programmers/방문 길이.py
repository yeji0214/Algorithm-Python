def solution(dirs):
    direction = {'U': [0, 1], 'D': [0, -1], 'R': [1, 0], 'L': [-1, 0]}
    visited = []
    cx, cy = 0, 0
    ans = 0
    
    for d in dirs:
        nx, ny = cx + direction[d][0], cy + direction[d][1]
        
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        if ((cx, cy),(nx, ny)) in visited or ((nx, ny),(cx, cy)) in visited:
            cx, cy = nx, ny
        else:
            ans += 1
            visited.append(((cx, cy),(nx, ny)))
            cx, cy = nx, ny
            
    return ans