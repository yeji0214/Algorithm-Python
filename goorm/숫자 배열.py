N = int(input())
arr = [[] * N for _ in range(N)]

for i in range(N):
	for j in range(N):
		arr[i].append(i*N + j+1)
	print(*arr[i])