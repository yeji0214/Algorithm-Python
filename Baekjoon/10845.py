N = int(input())
queue = []

for _ in range(N):
    command = input().split()
    c = command[0]

    if c == 'push':
        queue.append(command[1])
    elif c == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif c == 'size':
        print(len(queue))
    elif c == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif c == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif c == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])