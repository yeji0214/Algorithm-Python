a, b, n, k = map(int, input().split())

i = (k - 1) // (b * n) + 1
j = ((k - 1) % (b * n)) // n + 1

print(i, j)