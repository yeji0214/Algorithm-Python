# 구현, 그리디
N, M = map(int, input().split())
apple = []
s = 0
e = M-1
ans = 0

J = int(input())
for _ in range(J):
    apple.append(int(input()))

for i in apple:
    if s <= i - 1 <= e:
        continue
    elif e < i - 1:
        ans += i - 1 - e
        e = i - 1
        s = e - (M - 1)
    elif s > i - 1:
        ans += s - (i - 1)
        s = i - 1
        e = s + M - 1

print(ans)