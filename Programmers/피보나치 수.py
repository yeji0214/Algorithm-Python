def solution(n):
    f1 = 0
    f2 = 1
    f3 = f1 + f2
    
    for _ in range(2, n):
        f1 = f2
        f2 = f3
        f3 = f1 + f2
    
    return f3 % 1234567