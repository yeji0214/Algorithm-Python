S = input()
ans = ''

current = ''
tag = 0
for s in S:
    if s == '<':
        if current != '':
            ans += current[::-1]
        current = s
        tag = 1
    elif s == '>':
        current += s
        ans += current
        current = ''
        tag = 0
    elif tag == 1:
        current += s
    elif s == ' ' and current != '':
        ans += current[::-1]
        ans += ' '
        current = ''
    else:
        current += s

if current != '':
    ans += current[::-1]

print(ans)
