N = int(input())
files = list(input() for _ in range(N))
file = files[0]
ans = file

for i in range(1, N):
    ans = ''
    for j in range(len(file)):
        if file[j] != files[i][j] or file[j] == '?':
            ans += '?'
        else:
            ans += file[j]
    file = ans

print(ans)