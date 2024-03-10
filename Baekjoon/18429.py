# 내 풀이, 순열
from itertools import permutations

N, K = map(int, input().split())
A = list(map(int, input().split()))
arr = []
ans = 0
current = 500 # 현재 중량

for i in permutations(A, N):
    arr.append(list(i))

for i in range(len(arr)):
    for j in range(N):
        current = current - K + arr[i][j]
        if current < 500:
            break
    if current >= 500:
        ans += 1
    current = 500

print(ans)

# 다른 풀이 (백트래킹)
def bfs(weight, day):
   global ans

   if day == N: # 기간이 끝난 경우(모든 운동 키트 사용)
        ans += 1
        return
   
   if weight < 500:
       return
   
   for i in range(N):
       if not visited[i]:
           visited[i] = True
           bfs(weight-K+A[i], day+1)
           visited[i] = False
    

N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
visited = [False] * N

bfs(500, 0) # 현재 중량, 날짜

print(ans)