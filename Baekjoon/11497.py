# 그리디
# 통나무 건너뛰기의 난이도는 인접한 두 통나무 간의 높이의 차의 최댓값으로 결정됨. 난이도의 최소 구하기
# 접근 방식 : 통나무 높이의 내림차순으로 정렬, 가장 높은 통나무를 기준으로 양쪽으로 삽입
# 즉 최대값이 가운데, 양 옆으로 갈수록 점진적으로 줄어들게 설계

# 내 풀이
from collections import deque

T = int(input())

# 통나무 건너뛰기의 난이도가 최소가 되도록 정렬
def jump():
    while True:
        if len(L) == 0:
            return

        q.appendleft(L[0]) # 왼쪽 삽입
        L.pop(0)

        if len(L) == 0:
            return

        q.append(L[0]) # 오른쪽 삽입
        L.pop(0)

for _ in range(T):
    N = int(input())
    L = sorted(list(map(int, input().split())), reverse=True)
    q = deque()
    max_level = 0

    q.append(L[0]) # 가장 큰 값을 가운데에 삽입
    L.pop(0)

    jump()

    for i in range(N-1):
        max_level = max(max_level, abs(q[i] - q[i+1]))

    max_level = max(max_level, abs(q[0] - q[N-1]))

    print(max_level)


# 다른 풀이
T = int(input())

for _ in range(T):
    N = int(input())
    L = sorted(list(map(int, input().split())))
    max_level = 0

    for i in range(2, N):
        max_level = max(max_level, abs(L[i] - L[i-2]))

    print(max_level)