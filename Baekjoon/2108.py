import sys
from collections import Counter # 배열 각 요소의 데이터가 몇 번 등장하는지를 딕셔너리처럼 저장

input = sys.stdin.readline

N = int(input())
nums = []
ans = [] # 산술평균, 중앙값, 최빈값, 범위

for _ in range(N):
    nums.append(int(input()))

nums = sorted(nums)

ans.append(round(sum(nums) / N))
ans.append(nums[N // 2])

cnt = Counter(nums).most_common(2)
if len(cnt) > 1:
    if cnt[0][1] == cnt[1][1]:
        ans.append(cnt[1][0])
    else:
        ans.append(cnt[0][0])
else:
    ans.append(cnt[0][0])

ans.append(nums[-1] - nums[0])

print(*ans, sep='\n')