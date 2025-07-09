# 그리디, 정렬
N = int(input())
P = sorted(list(map(int, input().split())))
ans = 0

for i in range(1, N+1):
    ans += sum(P[:i])

print(ans)

###

N = int(input())
ans = 0

P = sorted(list(map(int, input().split())))

for i in range(N):
    ans += sum(P[:i + 1])

print(ans)