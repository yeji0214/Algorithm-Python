# 구현, 브루트포스
import copy

def change(x, y):
    result = 1

    for k in range(2):
        cx = x + dx[k]
        cy = y + dy[k]

        if 0 <= cx < N and 0 <= cy < N and candy[x][y] != candy[cx][cy]: # 범위 내에 있으면서 서로 다른 색의 사탕인 경우
            num = 1
            temp = copy.deepcopy(candy)
            temp[cx][cy], temp[x][y] = temp[x][y], temp[cx][cy]

            for a in range(N):
                # 행 검사
                current = temp[a][0]
                num = 1
                for b in range(1, N):
                    if current == temp[a][b]:
                        num += 1
                        result = max(result, num)
                    else:
                        current = temp[a][b]
                        num = 1

                # 열 검사
                current = temp[0][a]
                num = 1
                for b in range(1, N):
                    if current == temp[b][a]:
                        num += 1
                        result = max(result, num)
                    else:
                        current = temp[b][a]
                        num = 1

    return result

N = int(input())

candy = [[] * N for _ in range(N)]
ans = 1

dx = [1, 0]
dy = [0, 1]

for i in range(N):
    candy[i] = list(input())

for i in range(N):
    for j in range(N):
        ans = max(ans, change(i, j))

print(ans)