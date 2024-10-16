S = input()
P = input()
s = 0
e = 1
ans = 0

while len(P) > 0:
    while P[s:e] in S:
        e += 1
        if e > len(P):
            break
    ans += 1
    P = P[e-1:]
    s = 0
    e = 1

print(ans)