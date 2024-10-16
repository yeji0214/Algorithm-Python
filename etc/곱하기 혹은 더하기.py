S = list(map(int, input()))
ans = S[0]

for i in range(1, len(S)):
    if S[i] <= 1 or ans <= 1:
        ans += S[i]
    else:
        ans *= S[i]

print(ans)