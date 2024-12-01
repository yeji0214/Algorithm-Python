N = int(input())
arr = [[0] * 101 for _ in range(101)]

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

for _ in range(N):
    y, x, d, g = map(int, input().split())
    lst = [(x, y)]
    lst.append((x + di[d], y + dj[d]))
    for _ in range(g):
        ei, ej = lst[-1]
        for i in range(len(lst) - 2, -1, -1):
            ci, cj = lst[i]
            lst.append((ei - (ej - cj), ej + (ei - ci)))

    for i, j in lst:
        arr[i][j] = 1

ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == arr[i + 1][j] == arr[i][j + 1] == arr[i + 1][j + 1] == 1:
            ans += 1
print(ans)