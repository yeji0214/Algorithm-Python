T = int(input())
arr = []

for _ in range(T):
    parenthesis = list(input())
    no = 0
    arr = []
    for p in parenthesis:
        if p == '(':
            arr.append('(')
        else:
            if len(arr) == 0:
                print('NO')
                no = 1
                break
            arr.pop()
    if no == 0:
        if len(arr) == 0:
            print('YES')
        else:
            print('NO')