from collections import deque

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = True

    while q:
        c = q.popleft()
        if c == 100:
            return board[100]
        for i in range(1, 7):  # 나올 수 있는 주사위 수
            n = c + i  # 이동하게 될 좌표
            if n in special.keys():  # 사다리 또는 뱀을 만난 경우
                n = special[n]
            if n <= 100 and not visited[n]:  # 방문하지 않은 좌표인 경우
                visited[n] = True
                q.append(n)
                board[n] = board[c] + 1

    return board[100]

N, M = map(int, input().split())

special = {}
board = [0] * 101  # 1번부터 100번까지 사용
visited = [False] * 101  # 1번부터 100번까지 사용

for _ in range(N + M):
    num1, num2 = map(int, input().split())
    special[num1] = num2

print(bfs(1))  # 1번 칸에서 시작
