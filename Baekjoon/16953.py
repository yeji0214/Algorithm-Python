# 그리디, bfs
# 시간 초과 해결: B보다 작거나 같은 애만 deque에 저장 & visited 집합 사용해서 중복 방문 방지
from collections import deque

def move(q):
    nq = deque()
    while q:
        c = q.popleft()

        if c == B:
            return True
        
        if c * 2 <= B and (c * 2) not in visited:
            nq.append(c * 2)
            visited.add(c * 2)

        new_c = int(str(c) + '1')
        if new_c <= B and new_c not in visited:
            nq.append(new_c)
            visited.add(new_c)

    if not nq:
        return False

    return nq

A, B = map(int, input().split())
ans = 1
visited = {A}

q = deque()
q.append(A)

while True:
    m = move(q)
    if m == True:
        print(ans)
        exit(0)
    
    if m == False:
        print(-1)
        exit(0)

    q = m
    ans += 1