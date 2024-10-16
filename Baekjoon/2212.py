# 그리디, 정렬
N = int(input())
K = int(input())
sensor = sorted(list(map(int, input().split())))
distance = sorted([sensor[i] - sensor[i - 1] for i in range(1, N)])

print(sum(distance[:N-K]))