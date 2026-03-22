answer = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
N = int(input())
res = []

for i in range(N):
    num = list(map(int, input().split()))
    if num == answer:
        res.append(i + 1)

print(*res, sep='\n')