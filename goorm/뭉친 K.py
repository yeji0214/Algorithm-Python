from collections import deque

def bfs(x, y):
	q = deque()
	q.append((x, y))
	size = 0
	
	while q:
		cx, cy = q.popleft()
		size += 1
		
		for k in range(4):
			nx, ny = cx + dx[k], cy + dy[k]
			if 0 <= nx < N and 0 <= ny < N and M[nx][ny] == K:
				M[nx][ny] = -1
				q.append((nx, ny))
				
	sizes.append(size)

N = int(input())
x, y = map(int, input().split())
M = [[] * N for _ in range(N)]
sizes = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
	M[i] = list(map(int, input().split()))
	
K = M[x-1][y-1]
	
for i in range(N):
	for j in range(N):
		if M[i][j] == K:
			M[i][j] = -1
			bfs(i, j)
			
print(max(sizes))