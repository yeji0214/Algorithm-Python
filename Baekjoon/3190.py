N = int(input())
K = int(input())
arr = [[0] * N for _ in range(N)]
snake = [[0, 0]]
apple = []
conversion = {}
for _ in range(K):
    ax, ay = map(int, input().split())
    apple.append([ax - 1, ay - 1])
L = int(input())
for _ in range(L):
    X, C = input().split()
    conversion[int(X)] = C

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
forward = 0
time = 1

while True:
    nx, ny = snake[0][0] + direction[forward][0], snake[0][1] + direction[forward][1]

    if nx < 0 or nx >= N or ny < 0 or ny >= N or [nx, ny] in snake:
        print(time)
        exit(0)

    snake.insert(0, [nx, ny]) # 머리 이동

    if [nx, ny] in apple:
        apple.remove([nx, ny])
    else:
        snake.pop()

    if time in conversion.keys():
        if conversion[time] == 'D':
            forward += 1
            if forward == 4: forward = 0
        else:
            forward -= 1
            if forward == -1: forward = 3

    time += 1