def solution(wallpaper):
    file = []
    N, M = len(wallpaper), len(wallpaper[0])
    
    for i in range(N):
        for j in range(M):
            if wallpaper[i][j] == '#':
                file.append([i, j])
                
    x, y = [f[0] for f in file], [f[1] for f in file]
    
    return [min(x), min(y), max(x) + 1, max(y) + 1]