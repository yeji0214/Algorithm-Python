# 브루트포스
# 시간 초과 발생.. 섞으면 안되는 아이스크림의 번호를 각 인덱스에 저장하고 검사. 이중포문 안 돌게 변경
from itertools import combinations

N, M = map(int, input().split())
do_not_mix = [[] for _ in range(N+1)]
icecream = [x for x in range(1, N+1)]
three_icecream = []
ans = 0

for i in combinations(icecream, 3):
    three_icecream.append(list(i))

for _ in range(M):
    i1, i2 = map(int, input().split())
    do_not_mix[i1].append(i2)
    do_not_mix[i2].append(i1)

for i in range(len(three_icecream)):
    if three_icecream[i][1] in do_not_mix[three_icecream[i][0]] or three_icecream[i][2] in do_not_mix[three_icecream[i][0]] or three_icecream[i][1] in do_not_mix[three_icecream[i][2]]:
        continue
    ans += 1

print(ans)