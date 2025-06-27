A, B = map(int, input().split())
A = B - A

if A == B:
    print(0)
else:
    for i in range(A, 1, -1):
        if A % i == 0 and B % i == 0:
            A //= i
            B //= i
    print(A, B)