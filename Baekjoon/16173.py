from collections import deque

def bfs():
    q = deque()
    q.append((0, 0)) # 시작점
    visited[0][0] = True

    while q:
        cx, cy = q.popleft()
        jump = arr[cx][cy] # 이동할 칸 수

        if jump == 0: # 이 부분을 처리해주지 않으면 메모리 초과 발생
            continue

        # 오른쪽
        nx, ny = cx, cy + jump
        if nx == N - 1 and ny == N - 1:
            return "HaruHaru"
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            q.append((nx, ny))
            visited[nx][ny]

        # 아래
        nx, ny = cx + jump, cy
        if nx == N - 1 and ny == N - 1:
            return "HaruHaru"
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            q.append((nx, ny))
            visited[nx][ny]

    return "Hing"

N = int(input())
arr = [[] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))

print(bfs())

###


from collections import deque

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = True

    while q:
        cx, cy = q.popleft()
        move = m[cx][cy]
        nx, ny = cx + move, cy + move

        if 0 <= nx < N and not visited[nx][cy]:
            visited[nx][cy] = True
            q.append((nx, cy))
        if 0 <= ny < N and not visited[cx][ny]:
            visited[cx][ny] = True
            q.append((cx, ny))

    if visited[N - 1][N - 1]:
        return True
    else:
        return False

N = int(input())
m = [[] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]

for i in range(N):
    m[i] = list(map(int, input().split()))

if bfs():
    print("HaruHaru")
else:
    print("Hing")