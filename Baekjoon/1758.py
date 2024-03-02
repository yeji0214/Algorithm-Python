# 그리디, 정렬
N = int(input())
tips = []
ans = 0 

for _ in range(N):
    tips.append(int(input()))

tips.sort(reverse=True) # 내림차순 정렬

for i in range(0, len(tips)):
    tip = tips[i] - i
    if tip < 0:
        tip = 0
    ans += tip

print(ans)