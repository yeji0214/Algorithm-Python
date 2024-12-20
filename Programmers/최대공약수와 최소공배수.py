def solution(n, m):
    answer = []
    
    # 최대공약수
    mn = min(n, m)
    for i in range(mn, 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
    
    # 최소공배수
    mx = max(n, m)
    mul = 1
    current = mx
    while True:
        if current % n == 0 and current % m == 0:
            answer.append(current)
            break
        mul += 1
        current = mx * mul
        
    return answer

print(solution(6, 10))