# DP
n = int(input())

wine = list(int(input()) for _ in range(n))
drink = [0] * n

if n == 1:
    print(wine[0])
    exit(0)
elif n == 2:
    print(wine[0] + wine[1])
    exit(0)

drink[0] = wine[0]
drink[1] = wine[0] + wine[1]

for i in range(2, n):
    drink[i] = max(drink[i - 1], wine[i] + wine[i - 1] + drink[i - 3], wine[i] + drink[i - 2])

print(drink[n - 1])