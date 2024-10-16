# 백트래킹
N = int(input())
A = list(map(int, input().split()))
O = list(map(int, input().split()))

# 여기 1e9로 했을 때는 오류 났음 1e9 = 10억
maximum = -float('inf')
minimum = float('inf')

def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum

    if depth == N:
        maximum = max(maximum, total)
        minimum = min(minimum, total)
        return
    
    if plus:
        dfs(depth + 1, total + A[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - A[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * A[depth], plus, minus, multiply - 1, divide)
    if divide:
        if total < 0:
            dfs(depth + 1, -(abs(total) // A[depth]), plus, minus, multiply, divide - 1)
        else:
            dfs(depth + 1, total // A[depth], plus, minus, multiply, divide - 1)

dfs(1, A[0], O[0], O[1], O[2], O[3])
print(maximum)
print(minimum)