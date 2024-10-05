N, K = map(int, input().split())
num = list(input().rstrip())
delete = K
ans = []

for i in range(N):
    while delete and ans:
        if ans[-1] < num[i]:
            ans.pop()
            delete -= 1
        else:
            break
    ans.append(num[i])

print(''.join(ans[:N-K]))