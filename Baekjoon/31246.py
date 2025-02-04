import sys
input = sys.stdin.readline

N, K = map(int, input().split())
price = []

for _ in range(N):
    A, B = map(int, input().split())
    price.append(B - A)

price.sort()

if price[K - 1] < 0:
    print(0)
else:
    print(price[K - 1])