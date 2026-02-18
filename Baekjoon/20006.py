p, m = map(int, input().split())
rooms = []

for _ in range(p):
    l, n = input().split()
    l = int(l)
    belong = False

    if len(rooms) == 0: # 방이 하나도 없는 경우
        rooms.append([f'{l} {n}'])
        continue
    for i in range(len(rooms)):
        if len(rooms[i]) < m and abs(int(rooms[i][0].split()[0]) - l) <= 10:
            rooms[i].append(f'{l} {n}')
            belong = True
            break
    if not belong:
        rooms.append([f'{l} {n}'])

for r in rooms:
    r = sorted(r, key= lambda x: (x.split()[1]))
    if len(r) == m:
        print("Started!")
        print('\n'.join(r))
    else:
        print("Waiting!")
        print('\n'.join(r))