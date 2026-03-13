socks = []

for _ in range(5):
    socks.append(int(input()))

for s in socks:
    if socks.count(s) % 2 == 1:
        print(s)
        exit(0)