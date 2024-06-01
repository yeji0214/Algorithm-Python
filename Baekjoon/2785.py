# 그리디, 정렬
N = int(input())
L = sorted(list(map(int, input().split())))
ring = 0

if len(L) <= 3:
    ring = 1
else:
    while len(L) > 2:
        L[0] -= 1
        if L[0] < 0:
            L.pop(0)
            L[1] -= 1
        n1 = L.pop()
        n2 = L.pop()
        L.append(n1+n2)
        ring += 1
    if L[0] > 0:
        ring += 1

print(ring)