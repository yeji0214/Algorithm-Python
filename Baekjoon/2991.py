A, B, C, D = map(int, input().split())
P, M, N = map(int, input().split())

d1 = ''
d2 = ''

for i in range(A):
    d1 += 'O'
for i in range(B):
    d1 +='X'

for i in range(C):
    d2 += 'O'
for i in range(D):
    d2 +='X'

for k in P, M, N:
    idx1 = ((k - 1) + A + B) % (A + B)
    idx2 = ((k - 1) + C + D) % (C + D)
    if d1[idx1] == 'O' and d2[idx2] == 'O':
        print(2)
    elif d1[idx1] == 'X' and d2[idx2] == 'X':
        print(0)
    else:
        print(1)