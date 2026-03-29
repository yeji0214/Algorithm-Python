import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
Q = list(map(int, input().split()))

B = [0] * N
for i in range(N):
    B[i] = A[i] * A[(i + 1) % N] * A[(i + 2) % N] * A[(i + 3) % N]

ans = sum(B)

for q in Q:
    x = q - 1

    for i in [(x - 3) % N, (x - 2) % N, (x - 1) % N, x]:
        ans -= B[i]
        B[i] = -B[i]
        ans += B[i]

    print(ans)