def solution(board, h, w):
    answer = 0
    
    n = len(board)
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    color = board[h][w]
    
    for i in range(4):
        nx, ny = h + dx[i], w + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n and color == board[nx][ny]:
            answer += 1
    
    return answer