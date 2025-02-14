T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    
    f = N % H
    r = (N // H) + 1

    if f == 0:
        f = H
        r -= 1

    print(f * 100 + r)