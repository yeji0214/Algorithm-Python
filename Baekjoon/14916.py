# 그리디
n = int(input())
ans = 0

while n > 0:
    if n == 1: # 거슬러 줄 수 없음
        ans = -1
        break
    if n % 5 == 0: # 5로 나누어 떨어짐
        ans += n // 5
        break
    else:
        n -= 2
        ans += 1

print(ans)