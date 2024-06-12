K = int(input())
F = [0, 0, 1]

if K >= 3:
	for i in range(3, K+1):
		F.append(F[i-1] + F[i-2])
	
print(F[K] % 1000000007)