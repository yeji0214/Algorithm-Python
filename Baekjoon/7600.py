while True:
    sen = input()
    alphabet = []

    if sen == '#':
        exit(0)

    for s in sen:
        c = s.lower()
        if 'a' <= c <= 'z' and c not in alphabet:
            alphabet.append(c)

    print(len(alphabet))