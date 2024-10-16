# 그리디
N = int(input())
player = sorted(list(map(int, input().split()))) # 오름차순 정렬
energy = player[N:N+N]

print(energy[-1] - energy[0])