N, M, R = map(int, input().split())
arr = [[0] * M for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))

command = list(map(int, input().split()))

for com in command:
    current_r, current_c = len(arr), len(arr[0])

    if com == 1:
        new_arr = [[0] * current_c for _ in range(current_r)]
        for i in range(current_r):
            for j in range(current_c):
                new_arr[current_r - 1 - i][j] = arr[i][j]
        arr = new_arr
        continue

    if com == 2:
        new_arr = [[0] * current_c for _ in range(current_r)]
        for i in range(current_r):
            for j in range(current_c):
                new_arr[i][current_c - 1 - j] = arr[i][j]
        arr = new_arr
        continue

    if com == 3:
        new_arr = [[0] * current_r for _ in range(current_c)]
        for i in range(current_r):
            for j in range(current_c):
                new_arr[j][current_r - 1 - i] = arr[i][j]
        arr = new_arr
        continue

    if com == 4:
        new_arr = [[0] * current_r for _ in range(current_c)]
        for i in range(current_r):
            for j in range(current_c):
                new_arr[current_c - 1 - j][i] = arr[i][j]
        arr = new_arr
        continue

    # 4개의 배열로 분할
    mid_r, mid_c = current_r // 2, current_c // 2
    arr1 = [row[:mid_c] for row in arr[:mid_r]]
    arr2 = [row[mid_c:] for row in arr[:mid_r]]
    arr3 = [row[mid_c:] for row in arr[mid_r:]]
    arr4 = [row[:mid_c] for row in arr[mid_r:]]

    if com == 5:
        new_arr = [[0] * current_c for _ in range(current_r)]
        for i in range(mid_r):
            new_arr[i][:mid_c] = arr4[i]
        for i in range(mid_r):
            new_arr[i][mid_c:] = arr1[i]
        for i in range(mid_r, current_r):
            new_arr[i][mid_c:] = arr2[i - mid_r]
        for i in range(mid_r, current_r):
            new_arr[i][:mid_c] = arr3[i - mid_r]
        arr = new_arr
        continue

    if com == 6:
        new_arr = [[0] * current_c for _ in range(current_r)]
        for i in range(mid_r, current_r):
            new_arr[i][:mid_c] = arr1[i - mid_r]
        for i in range(mid_r):
            new_arr[i][:mid_c] = arr2[i]
        for i in range(mid_r):
            new_arr[i][mid_c:] = arr3[i]
        for i in range(mid_r, current_r):
            new_arr[i][mid_c:] = arr4[i - mid_r]
        arr = new_arr
        continue

for a in arr:
    print(*a)