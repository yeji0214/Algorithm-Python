# DP
N = int(input())
ans = 3

for i in range(1, N):
	ans *= 2
	
print(ans % 100000007)