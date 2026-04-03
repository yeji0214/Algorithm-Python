N = int(input())
ans = 0

for _ in range(N):
    d = int(input().split("D-")[1])
    if d <= 90:
        ans += 1

print(ans)