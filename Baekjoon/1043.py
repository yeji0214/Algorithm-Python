from collections import deque

def bfs(s):
    q = deque()
    for S in s:
        q.append(S)

    while q:
        c = q.popleft()

        for p in party:
            if c in p:
                for P in p:
                    if c != P and not know[P]:
                        know[P] = True
                        q.append(P)


N, M = map(int, input().split())
truth = list(map(int, input().split()))
know = [False] * (N + 1)
party = []
ans = 0

for i in range(1, len(truth)):
    know[truth[i]] = True

for _ in range(M):
    party.append(list(map(int, input().split()))[1:])

# 인접해있는 모든 사람들 구분
if len(truth) > 1:
    bfs(truth[1:])

# 파티원에 한 명이라도 있으면 거짓말 X
for p in party:
    exist = 0
    for P in p:
        if know[P]:
            exist = 1
            break
    if exist == 0:
        ans += 1
    
print(ans)