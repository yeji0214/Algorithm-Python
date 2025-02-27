M = int(input())
ans = 1

for _ in range(M):
    b1, b2 = map(int, input().split())
    if b1 == ans:
        ans = b2
    elif b2 == ans:
        ans = b1

print(ans)