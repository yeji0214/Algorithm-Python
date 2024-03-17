# 그래프, bfs
from collections import deque

def bfs(c):
    q = deque()
    q.append(c)

    while q:
        current = q.popleft()

        if color[current] == '': # 현재 좌표의 색이 없다면, 연결된 동그라미들의 색을 확인한 후 결정해야 함
            b_count = w_count = 0
            for k in arr[current]:
                if color[k] == 'B':
                    b_count += 1
                elif color[k] == 'W':
                    w_count += 1
                
            if b_count > 0 and w_count > 0:
                return 'impossible'
            elif b_count > 0 and w_count == 0:
                color[current] = 'W'
            else:
                color[current] = 'B'


        for k in arr[current]:
            if color[k] == '': # 아직 색이 정해지지 않은 동그라미인 경우
                if color[current] == 'B':
                    color[k] = 'W'
                else:
                    color[k] = 'B'
                q.append(k)
            elif color[k] == color[current]: # 연결된 동그라미와 색이 같은 경우
                return 'impossible'
    return 'possible'


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    arr = [[] for _ in range(n+1)]
    color = [''] * (n+1) # B or W

    for _ in range(m):
        n1, n2 = map(int, input().split())
        arr[n1].append(n2)
        arr[n2].append(n1)

    for i in range(1, n+1):
        if arr[i] != []:
            color[i] = 'B' # 시작
            s = i
            break

    ans = 0
    for i in range(s, n+1):
        if arr[i] != []:
            if bfs(i) == 'impossible':
                ans = 1

    if ans == 1:
        print('impossible')
    else:
        print('possible')