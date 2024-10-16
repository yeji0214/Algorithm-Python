# 그리디, 정렬
N, L = map(int, input().split())
h = sorted(list(map(int, input().split()))) # 오름차순 정렬

for i in h:
    if i <= L: # 자신의 길이보다 작거나 같은 높이에 있는 과일일 때
        L += 1

print(L)