# DP
MOD = 1000000007

def count_ways_to_reach(N):
	dp = [0] * (N + 1)
	dp[0] = 1 # 0번 칸에서 0번 칸으로 가는 방법은 1가지
	
	for i in range(1, N + 1):
		# 1칸 전에서 오는 경우
		if i - 1 >= 0:
			dp[i] += dp[i - 1]
		# 3칸 전에서 오는 경우
		if i - 3 >= 0:
			dp[i] += dp[i - 3]
			
		dp[i] %= MOD
			
	return dp[N]

# 예시 입력
N = int(input())
print(count_ways_to_reach(N))  # 결과 출력
