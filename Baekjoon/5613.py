ans = input()
ex = str(ans)

while True:
    s = input()

    if s == '=':
        print(ans)
        exit(0)

    elif s in ['+', '-', '*', '/']:
        if s == '/':
            ex += '//'
        else:
            ex += s

    else:
        ex += s
        ans = eval(ex)
        ex = str(ans)