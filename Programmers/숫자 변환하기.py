from collections import deque

def bfs(x, y, n, arr):
    q = deque()
    q.append(x)
    
    while q:
        c = q.popleft()
        for i in (c + n, c * 2, c * 3):
            if i == y:
                return arr[c] + 1
            elif i < y and arr[i] == 0:
                arr[i] = arr[c] + 1
                q.append(i)
                
    return -1

def solution(x, y, n):
    arr = [0] * (y + 1)
    
    if x == y:
        return 0
    
    return bfs(x, y, n, arr)