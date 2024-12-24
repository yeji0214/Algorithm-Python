N = int(input())
ans = 0

for n in range(1, N + 1):
    no = 0
    n = str(n)
    if len(n) <= 2:
        ans += 1
        continue
    gap = int(n[0]) - int(n[1])
    for x in range(1, len(n) - 1):
        if gap != (int(n[x]) - int(n[x + 1])):
            no = 1
            break
    if no == 0:
        ans += 1

print(ans)