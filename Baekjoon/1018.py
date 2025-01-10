N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
ans = 64

def chess():
    color = 'B'
    change = 0
    global ans

    for x in range(8):
        for y in range(8):
            if new_board[x][y] != color:
                change += 1
            if (x * 8 + y) % 8 != 7:
                if color == 'B': color = 'W'
                else: color = 'B'

    ans = min(ans, change)

    color = 'W'
    change = 0

    for x in range(8):
        for y in range(8):
            if new_board[x][y] != color:
                change += 1
            if (x * 8 + y) % 8 != 7:
                if color == 'B': color = 'W'
                else: color = 'B'

    ans = min(ans, change)


for i in range(N - 7):
    for j in range(M - 7):
        new_board = []
        for k in range(8):
            new_board.append(list(board[i + k][j:j+8]))
        chess()

print(ans)