n = int(input())
w = sorted(list(map(int, input().split())))
ans = []

for i in range(n):
    ans.append(w[i] + w[-(i+1)])

print(min(ans))