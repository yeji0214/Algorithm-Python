def solution(n):
    binary = str(bin(n)[2:])
    cnt = binary.count(1)
    ans = n
    
    while True:
        b = str(bin(ans)[2:])
        if cnt == b.count(1):
            return ans
        else:
            ans += 1

print(solution(78))