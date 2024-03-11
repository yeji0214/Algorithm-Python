# 투포인터
# 메모리 초과 발생. PyPy3로 하니까 됨
N = int(input())
num = [x for x in range(1, N+1)]
s, e = 0, 1
ans = 0

while s < e and s < N // 2:
    current = sum(num[s:e])
    if current < N:
        e += 1
    elif current > N:
        s += 1
    else:
        s += 1
        e = s + 1
        ans += 1
    
print(ans + 1)