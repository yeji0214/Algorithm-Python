# 그래프, bfs
from collections import deque

def bfs(s):
    visited[s] = True
    
    q = deque()
    q.append(s)

    while q:
        c = q.popleft()
        for k in member[c]:
            if not visited[k]:
                visited[k] = True
                score[k] = score[c] + 1
                q.append(k)

    final_score.append(max(score))


N = int(input())
member = [[] for _ in range(N+1)]
final_score = []

while True:
    m1, m2 = map(int, input().split())
    if m1 == -1 and m2 == -1:
        break
    member[m1].append(m2)
    member[m2].append(m1)

for i in range(1, N+1):
    visited = [False] * (N+1)
    score = [0] * (N+1)
    bfs(i)

leader_score = min(final_score) # 회장 후보의 점수
print(leader_score, final_score.count(leader_score))
for i in range(len(final_score)):
    if final_score[i] == leader_score:
        print(i+1, end=' ')