from collections import deque

def dfs():
    q = deque()
    invite[1] = True

    for f in friends[1]:
        if not invite[f]:
            invite[f] = True
            q.append(f)

    while q:
        c = q.popleft()
        for f in friends[c]:
            if not invite[f]:
                invite[f] = True

n = int(input())
m = int(input())

friends = [[] for _ in range(n + 1)]
invite = [False] * (n + 1)

for _ in range(m):
    f1, f2 = map(int, input().split())

    friends[f1].append(f2)
    friends[f2].append(f1)

if len(friends[1]) == 0:
    print(0)
    exit(0)

dfs()

print(invite.count(True) - 1)