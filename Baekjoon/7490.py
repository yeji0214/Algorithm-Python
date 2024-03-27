# 구현, 문자열, 브루트포스, 백트래킹
def dfs(n, s):
    if n == N:
        s += str(N)
        ns = ''.join(s.split())
        if eval(ns) == 0:
            ans.append(s)
        return
    
    dfs(n+1, s + str(n) + '+')
    dfs(n+1, s + str(n) + '-')
    dfs(n+1, s + str(n) + ' ')

T = int(input())

for _ in range(T):
    ans = []
    N = int(input())

    dfs(1, '') # 현재 숫자, 수식

    print(*sorted(ans), sep='\n')
    print()