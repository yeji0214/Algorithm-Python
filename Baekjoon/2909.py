C, K = map(int, input().split())
money = 10 ** K

if C % money == 0:
    print(C)
    exit(0)

m1, m2 = (C // money) * money, (C // money + 1) * money
ans = 0

if (C - m1) < (m2 - C):
    print(m1)
else:
    print(m2)