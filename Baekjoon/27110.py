N = int(input())
C = list(map(int, input().split()))
ans = 0

for c in C:
    if c < N:
        ans += c
    else:
        ans += N

print(ans)