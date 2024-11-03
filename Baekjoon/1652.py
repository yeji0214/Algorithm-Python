N = int(input())
room = ['.' * N for _ in range(N)]

width = 0
height = 0

for i in range(N):
    room[i] = list(input())
    lie = 0
    flag = 0
    
    for r in room[i]:
        if r == '.':
            lie += 1
        if r == 'X':
            lie = 0
            flag = 0
        if lie >= 2 and flag == 0:
            width += 1
            flag = 1

for i in range(N):
    room_Y = [row[i] for row in room]
    lie = 0
    flag = 0

    for r in room_Y:
        if r == '.':
            lie += 1
        if r == 'X':
            lie = 0
            flag = 0
        if lie >= 2 and flag == 0:
            height += 1
            flag = 1

print(width, height)