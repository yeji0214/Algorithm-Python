def solution(n, w, num):
    h = n // w
    if n % w > 0:
        h += 1
    arr = [[0] * w for _ in range(h)]
    
    for i in range(h):
        arr[i] = [number for number in range(w * i + 1, w * (i + 1) + 1)]
        
    for i in range(w):
        if arr[-1][i] > n:
            arr[-1][i] = 0
            
    for i in range(1, h, 2):
        arr[i] = arr[i][::-1]
        
    numx = numy = 0
    for i in range(h):
        if num in arr[i]:
            numx = i
            numy = arr[i].index(num)
    
    result_col = [a[numy] for a in arr[numx:]]
    return len(result_col) - result_col.count(0)