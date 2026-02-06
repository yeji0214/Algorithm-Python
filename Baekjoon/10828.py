# # 구현, 자료구조, 스택
# import sys
# N = int(sys.stdin.readline())
# stack = []

# for _ in range(N):
#     command = list(sys.stdin.readline().split())

#     if command[0] == 'push':
#         stack.append(command[1])
        
#     elif command[0] == 'pop':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack.pop(-1))

#     elif command[0] == 'size':
#         print(len(stack))

#     elif command[0] == 'empty':
#         if len(stack) == 0:
#             print(1)
#         else:
#             print(0)

#     elif command[0] == 'top':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack[-1])

from collections import deque
import sys

N = int(sys.stdin.readline())
q = deque()

for _ in range(N):
    cmd = list(sys.stdin.readline().split())
    
    if cmd[0] == 'push':
        q.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)