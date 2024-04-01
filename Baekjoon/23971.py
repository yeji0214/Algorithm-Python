# 수학, 사칙연산
H, W, N, M = map(int, input().split())

height = 0
width = 0

for i in range(1, H+1, N+1):
    height += 1

for i in range(1, W+1, M+1):
    width += 1

print(height*width)