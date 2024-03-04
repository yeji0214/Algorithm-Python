A, B = map(int, input().split())
N = int(input())
frequency = []
ans = 0

for _ in range(N):
    frequency.append(int(input()))

case1 = abs(A-B) # A에서 B로 바로 이동하는 경우
case2 = float('inf') # 다른 주파수를 거쳐서 이동하는 경우. 정수 최대값으로 초기화

for i in range(N):
    case2 = min(case2, abs(frequency[i] - B)) # B와 가장 가까운 주파수와 B의 차

if case1 <= case2:
    ans = case1
else:
    ans = case2 + 1 # 다른 주파수로 이동하기 위해 버튼을 클릭하므로 +1

print(ans)