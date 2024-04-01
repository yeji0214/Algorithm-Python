import sys

M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    command = sys.stdin.readline().split()

    c1 = command[0]

    if len(command) == 2:
        c2 = int(command[1])

        # add
        if c1 == 'add':
            S.add(c2)

        # remove
        elif c1 == 'remove':
            S.discard(c2)

        # check
        elif c1 == 'check':
            if c2 in S:
                print(1)
            else:
                print(0)

        # toggle
        elif c1 == 'toggle':
            if c2 in S:
                S.discard(c2)
            else:
                S.add(c2)
    else:
        # all
        if c1 == 'all':
            S = {i for i in range(1,21)}

        # empty
        elif c1 == 'empty':
            S = set()
            # S.clear()로 하니까 에러 발생했음