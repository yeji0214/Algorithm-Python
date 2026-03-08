N, M = map(int, input().split())
T, S = map(int, input().split())

z = N + (N // 8 - (N % 8 == 0)) * S
d = M + (M // 8 - (M % 8 == 0)) * (2 * T + S) + T

if z < d:
    print("Zip")
    print(z)
else:
    print("Dok")
    print(d)