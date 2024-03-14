# 그리디
K = int(input())
size = 0 # 구매해야하는 가장 작은 초콜릿의 크기
ans = 0 # 최소 몇 번 쪼개야 하는지
exponent = 0 # 현재 지수
arr = [] # 현재 초콜릿들의 사이즈

while True:
    if pow(2, exponent) >= K:
        size = pow(2, exponent)
        arr.append(size)
        break
    exponent += 1

goal_size = size - K
current_size = goal_size

while True:
    for i in arr:
        if current_size >= i:
            current_size -= i
    if current_size == 0:
        break
    current_size = goal_size
    arr.sort(reverse=True)
    min_num = arr.pop()
    arr.append(min_num // 2)
    arr.append(min_num // 2)
    ans += 1

print(size, ans)