N, L, D = map(int, input().split())
music = []

for _ in range(N):
    for _ in range(L):
        music.append(1)
    for _ in range(5):
        music.append(0)

idx = 0
while True:
    if idx >= len(music):
        break
    if music[idx] == 0:
        print(idx)
        exit(0)
    else:
        idx += D
print(idx)