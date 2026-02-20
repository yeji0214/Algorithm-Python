N = int(input())

for _ in range(N):
    yoda = list(input().split())
    res = yoda[2:] + yoda[:2]
    print(' '.join(res))