N, M = map(int, input().split())

packages = []
pieces = []
ans = float('inf')

for _ in range(M):
    price1, price2 = map(int, input().split())
    packages.append(price1)
    pieces.append(price2)

# 패키지와 낱개의 최소 가격 추출 (다른 값은 필요 X)
min_package = min(packages)
min_piece = min(pieces)

# 될 수 있는 케이스 3개 (패키지로만, 패키지 + 낱개, 낱개로만)
ans = min(ans, min_package * (N // 6 + 1)) # 패키지로만 구입
for i in range(1, (N // 6 + 1)): # 패키지 + 낱개 구입
    ans = min(ans, min_package * i + min_piece * (N - (6 * i)))
ans = min(ans, N * min_piece) # 낱개로만 구입

print(ans)