# 정렬
N = int(input())
coordinate = []

for _ in range(N):
    x, y = map(int, input().split())
    coordinate.append([x, y])

ans = sorted(coordinate, key=lambda x: (x[1], x[0]))

for i in ans:
    print(*i)