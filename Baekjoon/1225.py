# pypy로 통과
A, B = input().split()
ans = 0

for a in A:
    for b in B:
        ans += (int(a) * int(b))

print(ans)

# 시간초과 문제 해결 코드
A, B = input().split()
A_lst = map(int, A)
B_lst = map(int, B)

ans = sum(A_lst) * sum(B_lst)
print(ans)