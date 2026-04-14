N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

layer = 0
b = min(N, M) // 2

while layer < b:
    coords = []
    for i in range(layer, M-layer):
        coords.append((layer, i))
    for i in range(1 + layer, N - layer):
        coords.append((i, M - layer - 1))
    for i in range(M - (layer + 2), layer - 1, -1):
        coords.append((N - (1 + layer), i))
    for i in range(N - (layer + 2), layer, -1):
        coords.append((i, layer))

    arr = [A[x][y] for x, y in coords]
    r = R % len(arr)
    rotated_arr = arr[r:] + arr[:r]

    for x, y in coords:
        A[x][y] = rotated_arr.pop(0)

    layer += 1

for a in A:
    print(*a)