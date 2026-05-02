from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def bfs(x, y, oc, c):
            q = deque()
            q.append((x, y))
            image[x][y] = c
            visited[x][y] = True

            while q:
                cx, cy = q.popleft()

                for k in range(4):
                    nx, ny = cx + dx[k], cy + dy[k]

                    if 0 <= nx < len(image) and 0 <= ny < len(image[0]) and image[nx][ny] == oc and not visited[nx][ny]:
                        image[nx][ny] = c
                        visited[nx][ny] = True
                        q.append((nx, ny))


        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        visited = [[False] * len(image[0]) for _ in range(len(image))]

        bfs(sr, sc, image[sr][sc], color)

        return image