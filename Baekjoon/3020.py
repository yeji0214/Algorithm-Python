# 누적합, imos 알고리즘
import sys
input = sys.stdin.readline

N, H = map(int, input().split())

imos = [0] * (H + 1)

for i in range(N):
    o = int(input())
    if i % 2 == 0: # 짝수인 경우 (석순)
        imos[0] += 1
        imos[o] -= 1
    else: # 홀수인 경우 (종유석)
        imos[H-o] += 1
        imos[H] -= 1

now = 0
for i in range(H):
    now += imos[i]
    imos[i] = now

Min = min(imos[:H])
print(Min, imos.count(Min))