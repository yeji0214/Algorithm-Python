# 그리디, 정렬
N = int(input())
C = []
ans = 0

for _ in range(N):
    C.append(int(input()))

C = sorted(C, reverse=True) # 내림차순 정렬

while len(C) >= 3: # 한 번에 3개의 유제품을 사는 경우
    dairy = C[0:3]
    ans += sum(dairy) - min(dairy)
    del C[0:3]

if len(C) > 0: # 남은 유제품이 있다면
    ans += sum(C)

print(ans)