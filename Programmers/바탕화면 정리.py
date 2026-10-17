# def solution(wallpaper):
#     file = []
#     N, M = len(wallpaper), len(wallpaper[0])
    
#     for i in range(N):
#         for j in range(M):
#             if wallpaper[i][j] == '#':
#                 file.append([i, j])
                
#     x, y = [f[0] for f in file], [f[1] for f in file]
    
#     return [min(x), min(y), max(x) + 1, max(y) + 1]

def solution(wallpaper):
    for i in range(len(wallpaper)):
        if '#' in wallpaper[i]:
            lux = i
            break

    for i in range(len(wallpaper[0])):
        arr = [x[i] for x in wallpaper]
        if '#' in arr:
            luy = i
            break

    for i in range(len(wallpaper) - 1, -1, -1):
        if '#' in wallpaper[i]:
            rdx = i + 1
            break

    for i in range(len(wallpaper[0]) - 1, -1, -1):
        arr = [x[i] for x in wallpaper]
        if '#' in arr:
            rdy = i + 1
            break

    return [lux, luy, rdx, rdy]