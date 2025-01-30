N = int(input())
first_names = []
ans = []

for _ in range(N):
    first_names.append(input()[0])

for i in range(N):
    name = first_names[i]
    if first_names.count(name) >= 5 and name not in ans:
        ans.append(name)
    
if len(ans) == 0:
    print('PREDAJA')
else:
    print(*sorted(ans), sep='')