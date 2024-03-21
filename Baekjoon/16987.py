# 백트래킹, 브루트포스
def dfs(n):
    ans = 0

    if n == N: # 모든 계란을 검사한 경우 종료
        cnt = 0
        for i in range(N):
            if eggs[i][0] <= 0:
                cnt += 1
        return cnt
    
    if eggs[n][0] <= 0: # 현재 계란이 깨진 경우
        return dfs(n+1) # 다음 계란으로 이동
    
    # 껠 수 있는 계란이 있는지 검사
    egg = 0 
    for j in range(N):
        if n == j:
            continue
        if eggs[j][0] > 0:
            egg += 1
            break

    if egg == 0: # 깰 수 있는 계란이 없는 경우 다음 계란으로 이동
        return dfs(n+1)
    

    for k in range(N):
        if k != n and eggs[k][0] > 0: # 같은 계란이 아니면서 깰 수 있는 계란인 경우
            eggs[k][0] -= eggs[n][1]
            eggs[n][0] -= eggs[k][1]

            ans = max(ans, dfs(n+1))

            eggs[k][0] += eggs[n][1]
            eggs[n][0] += eggs[k][1]

    return ans


N = int(input())
eggs = []

for _ in range(N):
    S, W = map(int, input().split())
    eggs.append([S, W])

print(dfs(0)) # 현재 계란의 위치