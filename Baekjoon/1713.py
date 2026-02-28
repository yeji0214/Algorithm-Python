N = int(input())
M = int(input())
recommend = list(map(int, input().split()))
result = {}

for r in recommend:
    if result:
        for key in result:
            result[key][1] += 1
            
    if r in result:
        result[r][0] += 1
    else:
        if len(result) >= N:
            # 추천수 오름차순 -> 게시된 시간 내림차순
            result = dict(sorted(result.items(), key=lambda x: (x[1][0], -x[1][1])))
            del result[next(iter(result))]
            result[r] = [1, 1]
        else:
            result[r] = [1, 1]

print(*sorted(result.keys()))