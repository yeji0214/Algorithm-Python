import sys
input = sys.stdin.readline

N = int(input())
t = []

for _ in range(N):
    t.append(int(input()))

t = sorted(t, reverse=True)
ans = t[0]

for i in range(1, N):
    ans += t[i] - 1

print(ans)