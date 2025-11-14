from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))
    q = deque()

    for i in range(N):
        q.append((i, importance[i]))

    while True:
        first = q.popleft()

        if len(q) > 0 and first[1] < max(v for _,v in q):
            q.append(first)
        elif first[0] == M:
            print(N - len(q))
            break