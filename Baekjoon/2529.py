# 브루트포스, 백트래킹
def dfs(n, lst):
    if n == k+1: # 부등호 관계를 만족하는 정수가 만들어진 경우
        ans.append(lst)
        return
    
    for j in range(10):
        if not visited[j]:
            if n == 0:
                visited[j] = True
                dfs(n+1, lst + [j])
                visited[j] = False
            else:
                if eval(str(lst[n-1]) + inequality_sign[n-1] + str(j)):
                    visited[j] = True
                    dfs(n+1, lst + [j])
                    visited[j] = False

k = int(input())
inequality_sign = list(input().split())
visited = [False] * 10
ans = []

dfs(0, []) # 현재 넣은 숫자의 개수, 현재 리스트

print(*ans.pop(), sep='')
print(*ans.pop(0), sep='')