# 투포인터 ver
N, M = map(int, input().split())

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

a = 0
b = 0

ans = []

while a < N and b < M:
    if A[a] <= B[b]:
        ans.append(A[a])
        a += 1
    else:
        ans.append(B[b])
        b += 1

if a == N:
    ans += B[b:]
else:
    ans += A[a:]

print(*ans)


# 정렬 ver
N, M = map(int, input().split())
arr = []

for _ in range(2):
    arr += list(map(int, input().split()))

print(*sorted(arr))