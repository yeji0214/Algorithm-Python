# Y: 30초마다 10원
# M: 60초마다 15원
N = int(input())
call = list(map(int, input().split()))
y = 0
m = 0

for c in call:
    y += 10 + 10 * (c // 30)
    m += 15 + 15 * (c // 60)

if y > m:
    print(f'M {m}')
elif y < m:
    print(f'Y {y}')
else:
    print(f'Y M {y}')