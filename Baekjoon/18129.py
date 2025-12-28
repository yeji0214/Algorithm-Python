S, K = input().split()
S = S.lower()
K = int(K)
arr = []
ans = ''

prev = S[0]
cnt = 1
for i in range(1, len(S)):
    if prev == S[i]:
        cnt += 1
    else:
        if prev not in arr:
            arr.append(prev)
            if cnt >= K:
                ans += '1'
            else:
                ans += '0'
        cnt = 1
        prev = S[i]

if S[i] not in arr:
    arr.append(prev)
    if cnt >= K:
        ans += '1'
    else:
        ans += '0'

print(ans)