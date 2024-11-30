# 내 풀이
from itertools import product
import copy

def watch(location, com):
    temp = copy.deepcopy(arr)  # 원본 배열 복사
    for i in range(len(location)):
        cx, cy = location[i]  # CCTV 위치

        for direction in com[i]:  # 현재 CCTV의 감시 방향
            nx, ny = cx + direction[0], cy + direction[1]
            while 0 <= nx < N and 0 <= ny < M and temp[nx][ny] != 6:
                if temp[nx][ny] == 0:  # 감시할 수 있는 빈칸
                    temp[nx][ny] = -1  # 감시 중 표시
                # 다음 위치로 이동
                nx, ny = nx + direction[0], ny + direction[1]
    return temp

# 입력 처리
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cctv = []
cctv_location = []
ans = N * M

# 각 CCTV의 감시 방향 정의
cctv1 = [[(-1, 0)], [(1, 0)], [(0, -1)], [(0, 1)]]
cctv2 = [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]]
cctv3 = [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]]
cctv4 = [[(0, -1), (0, 1), (-1, 0)], [(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]]
cctv5 = [[(-1, 0), (1, 0), (0, -1), (0, 1)]]

# CCTV 위치와 종류 저장
for i in range(N):
    for j in range(M):
        if 1 <= arr[i][j] <= 5:
            cctv_location.append((i, j))
            if arr[i][j] == 1:
                cctv.append(cctv1)
            elif arr[i][j] == 2:
                cctv.append(cctv2)
            elif arr[i][j] == 3:
                cctv.append(cctv3)
            elif arr[i][j] == 4:
                cctv.append(cctv4)
            else:
                cctv.append(cctv5)

# 조합 생성
result = list(product(*cctv))  # CCTV 방향 조합 생성

# 각 조합에 대해 감시 영역 계산
for combination in result:
    blind = 0
    temp = watch(cctv_location, combination)

    # 사각지대 계산
    for i in range(N):
        blind += temp[i].count(0)
    ans = min(ans, blind)

print(ans)


# 다른 풀이
di = [-1,0,1,0]
dj = [0,1,0,-1]
cctv = [[], [1],[1,3],[0,1],[0,1,3],[0,1,2,3]]
def cal(tlst):
    v = [[0]*(M+2) for _ in range(N+2)]

    # 모든 CCTV에 대해서 처리(좌표, type, rot)
    for i in range(CNT):
        si,sj = lst[i]      # 1~N, 1~M
        rot = tlst[i]       # 0~3
        type = arr[si][sj]  # 1~5

        # type에 따른 모든 방향을 뻗어가면서 v[] 1표시
        for dr in cctv[type]:
            dr = (dr+rot)%4
            ci,cj = si,sj
            while True:
                ci,cj = ci+di[dr], cj+dj[dr]
                if arr[ci][cj]==6:  # 벽이면 그만 뻗어감
                    break
                v[ci][cj]=1

    # 사각지대(빈칸 0이고, 미방문) 개수 카운트
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if arr[i][j]==0 and v[i][j]==0:
                cnt+=1
    return cnt

def dfs(n, tlst):
    global ans
    if n==CNT:      # 모든 cctv의 방향(0~3) 정하기 완료
        ans = min(ans, cal(tlst))
        return

    dfs(n+1, tlst+[0])  #   0도 회전
    dfs(n+1, tlst+[1])  #  90도 회전
    dfs(n+1, tlst+[2])  # 180도 회전
    dfs(n+1, tlst+[3])  # 270도 회전

N, M = map(int, input().split())
# 벽(6번)으로 가장 자리를 막음
arr = [[6]*(M+2)]+[[6]+list(map(int, input().split()))+[6] for _ in range(N)]+[[6]*(M+2)]

# 1번~5번 CCTV를 저장
lst = []
for i in range(1, N+1):
    for j in range(1, M+1):
        if 1<=arr[i][j]<=5:
            lst.append((i,j))

CNT = len(lst)
ans = N*M
dfs(0, [])
print(ans)