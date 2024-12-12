def solution(n):
    binary = str(bin(n)[2:])
    cnt = binary.count('1')
    ans = n + 1
    
    while True:
        b = str(bin(ans)[2:])
        if cnt == b.count('1'):
            return ans
        else:
            ans += 1