computer = [0] * 101
N = int(input())
nums = list(map(int, input().split()))
ans = 0

for i in range(N):
    if computer[nums[i]] == 1:
        ans += 1
    else:
        computer[nums[i]] = 1

print(ans)