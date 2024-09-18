import sys
input = sys.stdin.readline

N = int(input())
lines = []
ans = 0

for _ in range(N):
    lines.append(tuple(map(int, input().split())))

lines.sort() # 정렬을 해주면 시작점은 비교할 필요가 없다

s, e = lines[0]

for i in range(1, N):
    x, y = lines[i]

    if x <= e: # 겹치는 경우
        e = max(y, e)

    else: # 겹치지 않는 경우
        ans += (e - s) # 기존 차이 더해주기
        s, e = x, y

ans += (e - s)
print(ans)