from collections import deque

def getDistance(sx, sy, ex, ey):
    return (abs(sx - ex) + abs(sy - ey))

def bfs(house):
    q = deque()
    q.append((house[0], house[1]))
    visited = []

    while q:
        cx, cy = q.popleft()

        if getDistance(cx, cy, rock[0], rock[1]) <= 1000:
            return "happy"

        for c in con:
            if getDistance(cx, cy, c[0], c[1]) <= 1000 and [c[0], c[1]] not in visited:
                q.append((c[0], c[1]))
                visited.append([c[0], c[1]])

    return "sad"

t = int(input())

for _ in range(t):
    n = int(input())
    house = list(map(int, input().split()))
    con = []
    for _ in range(n):
        c = list(map(int, input().split()))
        con.append([c[0], c[1]])

    rock = list(map(int, input().split()))

    print(bfs(house))