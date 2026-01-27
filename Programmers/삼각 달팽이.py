def solution(n):
    arr = [[0] * (i+1) for i in range(n)]
    move = [[1, 0], [0, 1], [-1 ,-1]]
    x, y = 0, 0
    num = 1
    direction = 0
    
    for step in range(n, 0, -1):
        for i in range(step):
            arr[x][y] = num
            x, y = x + move[direction][0], y + move[direction][1]
            num += 1
        x, y = x - move[direction][0], y - move[direction][1]
        direction = (direction + 1) % 3
        x, y = x + move[direction][0], y + move[direction][1]
        
    return sum(arr, [])