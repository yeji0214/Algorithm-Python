N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
	if A[i] % M != 0:
		A[i] *= M
		
print(*A)