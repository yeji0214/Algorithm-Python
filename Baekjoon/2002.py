# 구현, 문자열
# 내 풀이
N = int(input())
enter = [] # 차가 터널에 들어가는 순서대로
exit = [] # 차가 터널에서 나오는 순서대로
ans = 0

for _ in range(N):
    enter.append(input())

for _ in range(N):
    exit.append(input())

for i in exit:
    if i != enter[0]: # 차가 들어간 순서와 나오는 순서 불일치
        ans += 1
        enter.remove(i)

    else: # 일치
        enter.pop(0)

print(ans)