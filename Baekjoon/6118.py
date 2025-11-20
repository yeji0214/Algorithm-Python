# # 그래프, bfs
# from collections import deque

# def bfs(s):
#     q = deque()
#     q.append(s)
#     visited[s] = True

#     while q:
#         c = q.popleft()

#         for i in arr[c]:
#             if not visited[i]:
#                 visited[i] = True
#                 distance[i] = distance[c] + 1
#                 q.append(i)

# N, M = map(int, input().split())
# arr = [[] for _ in range(N+1)]
# visited = [False] * (N+1)
# distance = [0] * (N+1)

# for _ in range(M):
#     num1, num2 = map(int, input().split())
#     arr[num1].append(num2)
#     arr[num2].append(num1)

# bfs(1) # 시작점

# ans = max(distance) # 가장 먼 거리
# print(distance.index(ans), ans, distance.count(ans))

from collections import deque

def bfs():
    q = deque()
    q.append(1)
    visited[1] = True

    while q:
        c = q.popleft()

        for b in barn[c]:
            if not visited[b]:
                visited[b] = True
                distance[b] = distance[c] + 1
                q.append(b)

N, M = map(int, input().split())
barn = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
distance = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    barn[A].append(B)
    barn[B].append(A)

bfs()

max_d = max(distance)
result = [i for i in range(N + 1) if distance[i] == max_d]

print(sorted(result)[0], max_d, len(result))