# 구현, 그리디
# 정렬 문법 기억할 것 -> sorted(dict.items(), key=lambda x: (-x[1], x[0]))
# value를 기준으로 내림차순 정렬 후 key를 기준으로 오름차순 정렬 !
N, M = map(int, input().split())
DNA = []
ans = []
hamming_distance = 0

for i in range(N):
    DNA.append(input())

for i in range(M):
    lst = []
    dict = {}

    for j in range(N):
        lst.append(DNA[j][i])
    for j in range(N):
        if DNA[j][i] not in dict.keys():
            dict[DNA[j][i]] = lst.count(DNA[j][i])

    sorted_dict = sorted(dict.items(), key=lambda x: (-x[1], x[0]))
    ans.append(sorted_dict[0][0])

for i in range(N):
    for j in range(M):
        if ans[j] != DNA[i][j]:
            hamming_distance += 1

print(*ans, sep='')
print(hamming_distance)