# 그리디, 정렬

N = int(input())

grow = sorted(list(map(int, input().split())), reverse=True)
complete_grow = []

for i in range(N):
    complete_grow.append(grow[i] + (i+1))

print(max(complete_grow) + 1)