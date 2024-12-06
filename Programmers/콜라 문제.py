def solution(a, b, n):
    current = n
    ans = 0
    
    while a <= current:
        bottle = current // a * b
        current = current % a + bottle
        ans += bottle
        
    return ans