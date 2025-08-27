from collections import deque

def bfs(sx, sy, gx, gy, N, M, board, dx, dy, visited, ans):
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True
    
    while q:
        cx, cy = q.popleft()
        
        for i in range(4):
            nx, ny = cx, cy
            nnx, nny = nx + dx[i], ny + dy[i]
            
            while True: 
                if nnx < 0 or nnx >= N or nny < 0 or nny >= M or board[nnx][nny] == 'D':
                    break
                else:
                    nx, ny = nnx, nny
                    nnx, nny = nx + dx[i], ny + dy[i]
                
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:                
                visited[nx][ny] = True
                q.append((nx, ny))
                ans[nx][ny] = ans[cx][cy] + 1

                if nx == gx and ny == gy:
                    return ans[gx][gy]
            
    return -1
                

def solution(board):
    M, N = len(board[0]), len(board)
    visited = [[False] * M for _ in range(N)]
    ans = [[0] * M for _ in range(N)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(N):
        if 'R' in board[i]:
            sx, sy = i, board[i].find('R')
        if 'G' in board[i]:
            gx, gy = i, board[i].find('G')
            
    print(bfs(sx, sy, gx, gy, N, M, board, dx, dy, visited, ans))

solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."])