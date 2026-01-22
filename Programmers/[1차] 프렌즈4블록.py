def solution(m, n, board):
    board = [list(b) for b in board]
    ans = 0
    
    while True:
        remove = set()
        for i in range(len(board) - 1):
            for j in range(len(board[0]) - 1):
                a = board[i][j]
                b = board[i][j+1]
                c = board[i+1][j]
                d = board[i+1][j+1]

                if a == b == c == d != '':
                    index = [[i, j], [i, j+1], [i+1, j], [i+1, j+1]]
                    for idx in index:
                        remove.add((idx[0], idx[1]))

        if len(remove) == 0:
            return ans

        ans += len(remove)

        for i, j in remove:
            board[i][j] = ''

        for j in range(n):
            stack = []
            for i in range(m-1, -1, -1):
                if board[i][j] != '':
                    stack.append(board[i][j])
            for i in range(m-1, -1, -1):
                if stack:
                    board[i][j] = stack.pop(0)
                else:
                    board[i][j] = ''