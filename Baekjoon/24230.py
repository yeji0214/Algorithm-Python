import sys
input = sys.stdin.readline

N = int(input())
C = list(map(int, input().split()))

tree = [[] for _ in range(N)]
visited = [False for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

ans = 0

stack = []
stack.append(0)
visited[0] = True

# 루트 노드 색이 0이 아니면 초기값을 변경해야 하므로 먼저 카운팅
if C[0] != 0:
    ans += 1

while stack:
    node = stack.pop()
    for n in tree[node]:
        if not visited[n]:
            visited[n] = True  # 방문 처리는 여기서!
            stack.append(n)
            if C[node] != C[n]:  # 방문할 때 색상이 다르면 변경 횟수 증가
                ans += 1

print(ans)
