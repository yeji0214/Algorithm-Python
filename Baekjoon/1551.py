N, K = map(int, input().split())
arr = list(map(int, input().split(',')))

for _ in range(K):
    new_arr = []
    for i in range(1, len(arr)):
        new_arr.append(arr[i] - arr[i - 1])
    arr = new_arr

print(','.join(map(str, arr)))