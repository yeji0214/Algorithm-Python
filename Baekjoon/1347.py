N = int(input())
S = input()

minX = minY = 50
maxX = maxY = 50
x = y = 50
arr = [['#'] * 100 for _ in range(100)]
arr[50][50] = '.'

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dir = 2

for s in S:
    if s == 'L':
        dir = (dir - 1 + 4) % 4
    elif s == 'R':
        dir = (dir + 1 + 4) % 4
    else:
        x += dx[dir]
        y += dy[dir]
        arr[x][y] = '.'

        minX, minY = min(minX, x), min(minY, y)
        maxX, maxY = max(maxX, x), max(maxY, y)

for i in range(minX, maxX + 1):
    for j in range(minY, maxY + 1):
        print(arr[i][j], end='')
    print()