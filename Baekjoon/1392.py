N, Q = map(int, input().split())
time = 0
t = []

for _ in range(N):
    time += int(input())
    t.append(time - 1)

for _ in range(Q):
    q = int(input())
    for i in range(N):
        if q <= t[i]:
            print(i + 1)
            break