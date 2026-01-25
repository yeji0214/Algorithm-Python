def dfs(arr, x, y, size):
    first = arr[x][y]
    same = True
    
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != first:
                same = False
                break
        if not same:
            break
            
    if same:
        return (1, 0) if first == 0 else (0, 1)
    
    half = size // 2
    a0, a1 = dfs(arr, x, y, half)
    b0, b1 = dfs(arr, x + half, y, half)
    c0, c1 = dfs(arr, x, y + half, half)
    d0, d1 = dfs(arr, x + half, y + half, half)
    
    return (a0 + b0 + c0 + d0, a1 + b1 + c1 + d1)
    

def solution(arr):
    return list(dfs(arr, 0, 0, len(arr)))