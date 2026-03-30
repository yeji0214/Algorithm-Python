N = int(input())
name = ['PROBRAIN', 'GROW', 'ARGOS', 'ADMIN', 'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY']
max_q = 0
ans = ''

for i in range(9):
    r = list(map(int, input().split()))

    if max(r) > max_q:
        max_q = max(r)
        ans = name[i]

print(ans)