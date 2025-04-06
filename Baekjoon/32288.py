n = int(input())
nickname = input()
ans = ''

for n in nickname:
    if n == 'I':
        ans += 'i'
    else:
        ans += 'L'

print(ans)