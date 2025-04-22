S = input()
ans = []

for i in range(97, 123):
    a = chr(i)
    idx = S.find(a)
    if idx == -1:
        ans.append(-1)
    else:
        ans.append(idx)

print(*ans)