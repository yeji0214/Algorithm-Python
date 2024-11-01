N = int(input())
checkpoint = []
checkpoint_sum = 0
max_distance = 0

for _ in range(N):
    x, y = map(int, input().split())
    checkpoint.append([x, y])

ans = float('inf')

for i in range(N - 1):
    checkpoint_sum += (abs(checkpoint[i][0] - checkpoint[i+1][0]) + abs(checkpoint[i][1] - checkpoint[i+1][1]))

for i in range(1, N - 1):
    original_distance = abs(checkpoint[i - 1][0] - checkpoint[i][0]) + abs(checkpoint[i - 1][1] - checkpoint[i][1]) + abs(checkpoint[i][0] - checkpoint[i + 1][0]) + abs(checkpoint[i][1] - checkpoint[i + 1][1])
    new_distance = abs(checkpoint[i - 1][0] - checkpoint[i + 1][0]) + abs(checkpoint[i - 1][1] - checkpoint[i + 1][1])

    max_distance = max(max_distance, original_distance - new_distance)

print(checkpoint_sum - max_distance)