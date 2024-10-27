from collections import deque
import sys

input = sys.stdin.readline
N, K = map(int, input().split())

v = [-1] * (100000 + 1)
v[N] = 0
res = 0

q = deque()
q.append(N)

while q:
    current = q.popleft()

    if current == K:
        res += 1

    move = [current - 1, current + 1, current * 2]
    for m in move:
        if m < 0 or m > 100000:
            continue
        if v[m] == -1 or v[m] >= v[current] + 1:
            v[m] = v[current] + 1
            q.append(m)

print(v[K])
print(res)