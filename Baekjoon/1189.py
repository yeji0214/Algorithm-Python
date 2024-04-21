# 그래프, 브루트포스, 백트래킹
# 첫 번째 풀이
def dfs(x, y, d):
    global ans

    if x == 0 and y == C - 1:
        count_T = 0
        for i in range(R):
            count_T += visited[i].count(True)
        if count_T == K - 1:
            ans += 1
            return
        
    if x < 0 or x >= R or y < 0 or y >= C:
        return
    
    if arr[x][y] == '.' and not visited[x][y]:
        visited[x][y] = True
        dfs(x-1, y, d + 1)
        dfs(x+1, y, d + 1)
        dfs(x, y-1, d + 1)
        dfs(x, y+1, d + 1)
        visited[x][y] = False


R, C, K = map(int, input().split())
arr = [[] * C for _ in range(R)]
visited = [[False] * C for _ in range(R)]
ans = 0

for i in range(R):
    arr[i] = list(input())

arr[0][C-1] = 'G'
dfs(R-1, 0, 1) # 현재 좌표, 현재 거리

print(ans)


# 두 번째 풀이
def dfs(x, y, d):
    global ans

    if x == 0 and y == C - 1 and d == K:
        ans += 1
        return
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] == '.':
            arr[nx][ny] = '!'
            dfs(nx, ny, d+1)
            arr[nx][ny] = '.'

R, C, K = map(int, input().split())
arr = [[] * C for _ in range(R)]
ans = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(R):
    arr[i] = list(input())

arr[R-1][0] = 'S'
dfs(R-1, 0, 1) # 현재 좌표, 현재 거리

print(ans)