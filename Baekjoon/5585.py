# 그리디
money = 1000 - int(input())
moneys = [500, 100, 50, 10, 5, 1]
ans = 0

for i in moneys:
    ans += money // i
    money %= i

print(ans)