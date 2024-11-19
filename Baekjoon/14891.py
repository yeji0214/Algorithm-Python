def rotation_left(num, dir):
    global rotation_list
    while True:
        n_num = num - 1
        if n_num < 1:
            return
        else:
            if cogwheel[num - 1][6] != cogwheel[n_num - 1][2]:
                rotation_list.append([n_num, -dir])
                num = n_num
                dir = -dir
            else:
                return
            
def rotation_right(num, dir):
    global rotation_list
    while True:
        n_num = num + 1
        if n_num > 4:
            return
        else:
            if cogwheel[num - 1][2] != cogwheel[n_num - 1][6]:
                rotation_list.append([n_num, -dir])
                num = n_num
                dir = -dir
            else:
                return
            
def rotation(lst):
    global cogwheel

    for l in lst:
        num, dir = l
        if dir == 1:
            cogwheel[num - 1] = [cogwheel[num - 1][7]] + cogwheel[num - 1][:7]
        else:
            cogwheel[num - 1] = cogwheel[num - 1][1:] + [cogwheel[num - 1][0]]

cogwheel = []
score = {0: 1, 1: 2, 2: 4, 3: 8}
ans = 0

for _ in range(4):
    cogwheel.append(list(map(int, input())))

K = int(input())
for _ in range(K):
    num, dir = map(int, input().split())
    rotation_list = [[num, dir]]
    rotation_left(num, dir)
    rotation_right(num, dir)
    rotation(rotation_list)

for c in range(4):
    if cogwheel[c][0] == 1:
        ans += score[c]

print(ans)