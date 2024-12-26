import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque()

for _ in range(N):
    command = sys.stdin.readline().split()
    c = command[0]

    if c == 'push_front':
        q.appendleft(command[1])
    elif c == 'push_back':
        q.append(command[1])
    elif c == 'pop_front':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif c == 'pop_back':
        if not q:
            print(-1)
        else:
            print(q.pop())
    elif c == 'size':
        print(len(q))
    elif c == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif c == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif c == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])