from itertools import combinations

def getDistance(mbti):
    res = list(map(list,combinations(mbti, 3)))
    ans = 12

    for r in res:
        current = len(set(r[0] + r[1])) + len(set(r[1] + r[2])) + len(set(r[0] + r[2])) - 12
        ans = min(current, ans)

    return ans

T = int(input())

for _ in range(T):
    N = int(input())
    mbti = list(input().split())

    if N >= 33:
        print(0)
        continue

    print(getDistance(mbti))