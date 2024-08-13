N = int(input())
sugar = 0
ans = 0

# 이 부분을 고려하지 않아서 틀렸었음 (5로만 나누어지는 경우)
if N % 5 == 0:
    print(N // 5)
else:
    while N > 0:
        sugar += 3
        N -= 3
        ans += 1
        if N % 5 == 0:
            ans += N // 5
            N = 0

    if N != 0:
        print(-1)
    else:
        print(ans)