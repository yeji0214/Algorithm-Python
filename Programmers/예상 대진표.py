def solution(n,a,b):
    answer = 0
    
    while True:
        answer += 1
        p1, p2 = min(a, b), max(a, b)
        if p2 - p1 == 1 and p1 % 2 == 1 and p2 % 2 == 0:
            return answer
        if a % 2 == 0:
            a //= 2
        elif a % 2 == 1:
            a = a // 2 + 1
        if b % 2 == 0:
            b //= 2
        elif b % 2 == 1:
            b = b // 2 + 1