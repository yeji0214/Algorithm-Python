A, B, C = map(int, input().split())
T = int(input())

if T <= 30:
    print(A)
    exit(0)

r = T - 30
if r % B == 0:
    extra = r // B
else:
    extra = r // B + 1

print(A + C * extra)