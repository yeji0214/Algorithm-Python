N = int(input())

for _ in range(N):
    str = input()
    s = str.split()

    if s[0] == 'Simon' and s[1] == 'says':
        print(str[10:])