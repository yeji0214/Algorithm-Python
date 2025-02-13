vow = ['a', 'e', 'i', 'o', 'u']

while True:
    ans = 0
    sentence = input()
    if sentence == '#':
        exit(0)

    for s in sentence:
        if s.lower() in vow:
            ans += 1

    print(ans)