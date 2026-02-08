N = int(input())
sang = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))
dic = {}
ans = []

for s in sang:
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

for n in nums:
    if n not in dic:
        ans.append(0)
    else:
        ans.append(dic[n])

print(*ans)