while True:
    S = input()
    if S == '#':
        exit(0)
    alphabet = S[0]
    sentence = S[2:].lower()
    ans = 0

    for s in sentence:
        if s == alphabet:
            ans += 1

    print(alphabet, ans)