P = int(input())
ans = [0] * 4

for _ in range(P):
    G, C, N = map(int, input().split())
    if G == 1:
        ans[3] += 1
    elif C == 1 or C == 2:
        ans[0] += 1
    elif C == 3:
        ans[1] += 1
    else:
        ans[2] += 1

print(*ans, sep='\n')