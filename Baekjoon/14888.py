def dfs(n, sm, add, sub, mul, div):
    global maximum, minimum

    if n == N:
        maximum = max(maximum, sm)
        minimum = min(minimum, sm)
        return
    
    if add > 0:
        dfs(n + 1, sm + A[n], add - 1, sub, mul, div)
    if sub > 0:
        dfs(n + 1, sm - A[n], add, sub - 1, mul, div)
    if mul > 0:
        dfs(n + 1, sm * A[n], add, sub, mul - 1, div)
    if div > 0:
        dfs(n + 1, int(sm / A[n]), add, sub, mul, div - 1)

N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

maximum = -float('inf')
minimum = float('inf')

dfs(1, A[0], add, sub, mul, div)
print(maximum)
print(minimum)