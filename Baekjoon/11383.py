N, M = map(int, input().split())
str = []
res = []

for _ in range(N):
    str.append(input())

for _ in range(N):
    res.append(input())

for i in range(N):
    ans = ''
    for s in str[i]:
        ans += s * 2
    if res[i] != ans:
        print("Not Eyfa")
        exit(0)
print("Eyfa")