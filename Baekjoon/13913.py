from collections import deque

def bfs():
    q = deque()
    q.append(N)
                 
    while q:
        x = q.popleft()

        if x == K:
            ans = visited[x]
            cur_node = x
            way.append(x)

            while True:
                if cur_node == N:
                    break
                way.append(move[cur_node])
                cur_node = move[cur_node]

            print(ans)
            for w in way[::-1]:
                print(w, end=" ")
            break

        arr = [x + 1, x - 1, x * 2]

        for a in arr:
            if 0 <= a <= 200000 and visited[a] == 0:
                move[a] = x
                visited[a] = visited[x] + 1
                q.append(a)

    return ans


N, K = map(int, input().split())
visited = [0] * 200001
move = [0] * 200001 # 부모 노드 저장
ans = 100001
way = []

bfs()