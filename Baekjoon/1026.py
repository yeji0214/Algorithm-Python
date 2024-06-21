N = int(input())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))

ans = 0

for i in range(N):
    ans += A[i] * max(B)
    B[B.index(max(B))] = -1

print(ans)