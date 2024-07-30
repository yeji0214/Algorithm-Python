def solution(price, money, count):
    ans = 0
    need = 0
    
    for i in range(1, count + 1):
        need += price * i
        
    if need > money:
        ans = need - money
    
    return ans