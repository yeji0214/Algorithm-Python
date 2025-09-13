# for문 돌면서 매번 sum을 해줬을 때는, 시간 초과
N, K = map(int, input().split())
nums = list(map(int, input().split()))
res = []
res.append(sum(nums[:K]))

for i in range(N - K):
    res.append(res[i] - nums[i] + nums[i + K])

print(max(res))