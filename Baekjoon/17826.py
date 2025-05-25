scores = list(map(int, input().split()))
h = int(input())

res = scores.index(h) + 1

if res <= 5:
    print("A+")
    exit(0)
elif res <= 15:
    print("A0")
    exit(0)
elif res <= 30:
    print("B+")
    exit(0)
elif res <= 35:
    print("B0")
    exit(0)
elif res <= 45:
    print("C+")
    exit(0)
elif res <= 48:
    print("C0")
    exit(0)
else:
    print("F")
    exit(0)