# 그리디
N = int(input())
crane = sorted(list(map(int, input().split())), reverse=True)
M = int(input())
box = sorted(list(map(int, input().split())), reverse=True)
visited = [False] * (N + 1)
ans = 0
s = 0

if crane[0] < box[0]:
    print(-1)
    exit(0)
else:
    while len(box) > 0:
        for i in range(N):
            for j in range(len(box)):
                if box[j] <= crane[i]:
                    box.pop(j)
                    break
        ans += 1

print(ans)